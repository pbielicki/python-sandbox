fruits = 'pomme; poire  ; peche;\tabricot'


print fruits.split()
print fruits.split(';')
print fruits.split(';', 1)
print fruits.split('; ')
fruit_list = [f.strip() for f in fruits.split(';')]
print fruit_list

for fruit in fruit_list:
    print fruit,
print
