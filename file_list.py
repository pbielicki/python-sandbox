import os

blacklist = ['.svn', '.project']

for dirpath, dirnames, filenames in os.walk(os.getcwd()):
    print "%s: %s dirs / %s files" % (dirpath, len(dirnames), len(filenames))
    
    for blacklisted in blacklist:
        if blacklisted in dirnames:
            dirnames.remove(blacklisted)
            
print

def visit(arg, dirname, names):
    for filename in names:
        print os.path.join(dirname, filename)

os.path.walk(os.getcwd(), visit, 'unused')
