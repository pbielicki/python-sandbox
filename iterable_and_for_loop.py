"do not eat up memory - do not create list of 1000 elements"
for i in xrange(1000):
    print i
    
books = [("dupa", "cycek"),
         ("kicha", "mycha")]

for key, value in books:
    print key, ": ", value
    
"enumerate"
for i, value in enumerate(['foo', 'bar', 'dupa']):
    print i, " ", value

"zip"
for tup in zip(['foo', 'bar', 'dupa'], ['1', '2', '3']):
    print tup