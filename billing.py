import os, sys, tarfile

class Recoverer(object):
    def __init__(self):
        self.recovered = {}
        self.not_recovered = {}
        self.missing = {}

        self.f_rec = 'billing_recovered.log'
        self.f_mis = 'billing_missing.log'

        if os.path.exists(self.f_rec):
            print self.f_rec, 'exists'
            sys.exit(-1)
        
        if os.path.exists(self.f_mis):
            print self.f_mis, 'exists'
            sys.exit(-1)
        
        try:
            self.recovered_log = open('billing_recovered.log', 'w')
            self.not_recovered_log = open('billing_missing.log', 'w')
        except (IOError), e:
            print e
            sys.exit(-1)

    """ Returns map of missing ranges.
    Key is BE ID and value is a list of ranges. 
    """
    def _read_missing_report(self):
        try:
            f = open(sys.argv[1], 'r')
        except (IOError), e:
            print e
            sys.exit(-1)
    
        try:
            for line in f:
                split = line.split(' ')
                if len(split) != 3:
                    print 'Error in line ', split[0]
                    continue
    
                val = (int(split[1]), int(split[2]))
                range_list = self.missing.get(split[0], [])
                if len(range_list) == 0:
                    self.missing[split[0]] = range_list    
                # appending range tuple
                range_list.append(val)
                if len(self.not_recovered.get(split[0], [])) == 0:
                    self.not_recovered[split[0]] = []
                
                range_list = self.not_recovered[split[0]]
                for x in range(val[0], val[1] + 1):
                    range_list.append(x)

                self.not_recovered[split[0]] = sorted(set(range_list))
                
        finally:
            f.close()
    
    """ Finds missing entries in given file.
    Automatically unpacks and reads tar compressed files on the fly.
    """
    def _find_missing(self, path):
        if path.endswith('.tgz') or path.endswith('.gz'):
            try:
                tar = tarfile.open(path, 'r:*')
            except (IOError), e:
                print 'Unable to open "', path, '" file', e
                sys.exit(-1)
                
            try:
                for tarinfo in tar:
                    if tarinfo.isreg():
                        for line in tar.extractfile(tarinfo.name).readlines():
                            self._process_line(line, path + ":" + tarinfo.name)
            finally:
                tar.close()
        else:
            try:
                f = open(path, 'r')
            except (IOError), e:
                print 'Unable to open "', path, '" file', e
                sys.exit(-1)
        
            try:
                for line in f:
                    self._process_line(line, path)
            finally:
                f.close()

    """ Processes single line.
    """
    def _process_line(self, line, path):
        be_id = line[21:32]
        sequence = int(line[33:line.find('TID') - 1])
        range_list = self.missing.get(be_id, [])

        for val in range_list:
            if sequence >= val[0] and sequence <= val[1]:
                if len(self.recovered.get(be_id, [])) == 0:
                    self.recovered[be_id] = []
                
                self.recovered[be_id].append((sequence, path))
                try:
                    self.not_recovered[be_id].remove(sequence)
                except (ValueError):
                    x = 0 # empty line (nop) does not exists in Python                
                finally:
                    print line.rstrip()
    
    
    """ Dumps the report on not recovered items to file.
    """    
    def _report_recovered(self):
        for key, value in self.recovered.items():
            value = sorted(value)
            files = set([])
            dups = 0
            last = -1
            start = -1
            for seq, path in value:
                files.add(path)
                if last == -1:
                    last = start = seq
                    continue
                    
                if seq != last + 1 and seq != last:
                    self.recovered_log.write(self._format_msg(key, start, last, dups, files))
                    start = seq

                if seq == last:
                    dups += 1
                             
                last = seq
            
            if (start > -1):
                self.recovered_log.write(self._format_msg(key, start, last, dups, files))
                
        self.recovered_log.close()
        
    def _format_msg(self, key, start, last, dups, files):
        string = key + ' ' + str(start) + " - " + str(last) + ' recovered with ' + str(dups) + ' duplicates from: '
        i = 0
        for f in files:
            if i > 0:
                string += ', '
                
            string += f
            i += 1
            if i > 5:
                string += ' ...'
        
        string += '\n'
        return string
                                
    """ Dumps the report on not recovered items to file.
    """    
    def _report_not_recovered(self):
        for key, value in self.not_recovered.items():
            last = -1
            start = -1
            for seq in value:
                if last == -1:
                    last = start = seq
                    continue
                    
                if seq != last + 1:
                    self.not_recovered_log.write(key + ' ' + str(start) + " - " + str(last) + '\n')
                    start = seq
                    
                last = seq
            
            if start > -1:
                self.not_recovered_log.write(key + ' ' + str(start) + " - " + str(last) + '\n')

        self.not_recovered_log.close()
    
    """ Used to traverse recursively given directory.
    """
    def _visit(self, arg, dirname, names):
        for filename in names:
            path = os.path.join(dirname, filename)
            if os.path.isfile(path):
                self._find_missing(path)
                
    """ Class launcher.
    """
    def recover(self):
            if len(sys.argv) > 2:
                # missing variable contains map of list of ranges of missing records where key is BE id and value is the list of tuples
                self._read_missing_report()
            else:
                print 'Provide a file with missing records list and directory containing missing records'
                sys.exit(-1)
        
            os.path.walk(sys.argv[2], self._visit, None)
            
            self._report_recovered()
            self._report_not_recovered()

if __name__ == "__main__":
    rec = Recoverer()
    rec.recover()
