import sys

def parse_file():
    try:
        f_in = open(sys.argv[1], 'r')
        f_out = open('out.txt', 'w')
        f_junk = open('junk.txt', 'w')
    except (IOError), e:
        print e
        sys.exit(-1)
        
    for _num, line in enumerate(f_in):
        if (line.find('      ') > -1):
            f_out.write(line.split('      ')[1]
                        .strip().replace(' ', '')
                        .replace(',', '.') + '\n')
        else:
            if (line.find(',') > -1):
                f_junk.write(line)
        
if __name__ == "__main__":
    if len(sys.argv) > 1:
        parse_file()
    else:
        print 'Provide a file name'