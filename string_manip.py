fruits = "apple, orange, banana,pear"

print fruits.split()
print [f.strip() for f in fruits.split(",")]

print fruits.replace("apple", "pineapple")

a = fruits.split(',')
print a
c = '; '.join(a)
print c

print c.partition('; ');