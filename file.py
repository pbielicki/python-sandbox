f = open('file.txt', 'w')
for i in range(2):
    f.write('line %d\n' % i)
    
f.close()

f = open('file.txt', 'r')
for line in f:
    print line,