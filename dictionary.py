d = {'one': 1, 'two': 2, 'four': 4, 'three': 3}

print d
print d['two']

d['ten'] = 10
print d

print d.get('dupa')
print d.get('dupa', 'default')
print 'dupa' in d

for key, value in d.items():
    print key, ' = ', value