import sys

class ConfigExecption(Exception):
    pass

def read_config():
    result = {}
    try:
        f = open(sys.argv[1], 'r')
    except (IOError), e:
        print e
        sys.exit(-1)
        
    for num, line in enumerate(f):
        if (line.startswith('#') or len(line.strip()) == 0):
            continue
        
        split = line.split(' : ')
        if (len(split) != 2):
            raise ConfigExecption(f.name, "line %d" % num)
            
        result[split[0]] = split[1].rstrip()
        
    return result

if __name__ == "__main__":
    if len(sys.argv) > 1:
        print read_config()
    else:
        print 'Provide a file name'