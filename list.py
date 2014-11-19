# -*- coding: utf-8 -*-
fruits = ['apple',
          'Pear',
          'Banana',
          'pomarańcza']

fruits.append("dupa")
fruits.insert(2, "jabłko")
#del fruits[1]
fruits.remove("jabłko")
fruits.sort()

for s in fruits:
    print s

print fruits

"sorting with key function"
def tolower(s):
    return s.lower();

fruits.sort(key=tolower)
print fruits
fruits.reverse();
print fruits

print
print fruits.pop()
print fruits.pop()

print range(0, 100, 5)