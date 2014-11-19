"""
configuration file parser


write a parse_config function, taking a filename as argument and returning
a dictionary of configuration values

The file is formatted as

config_var_name : value

it can contain comments which start with a '#' char and go to the
end of the line.

if errors are detected during the parse, a custom exception ConfigParseError
must be raised, containing information about the file name and the line number.

"""

class ConfigParseError(Exception):
    pass
    # raise ConfigParseError(filename, lineno, message)

def parse_config(filename):
    fobj = open(filename)
    config = {}
    for lineno, line in enumerate(fobj):
        line, _hash, _comment = line.partition('#')
        # alternative version of above line:
        #line = line.split('#', 1)[0]
        line = line.strip()
        if not line:
            continue
        varname, colon, value = line.partition(':')
        if colon != ':':
            raise ConfigParseError(filename, lineno+1,
                                   'malformed line (no ":" found)')
        config[varname.strip()] = value.strip()
        
    fobj.close()
    return config

def test():
    print parse_config('config2.conf')
    try:
        print parse_config('config1.conf')
    except ConfigParseError, exc:
        print exc

if __name__ == '__main__':
    test()
