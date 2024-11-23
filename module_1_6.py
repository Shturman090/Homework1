my_dict={'Vasya': 1975, 'Egor': 1999, 'Masha': 2002}
print(my_dict)

print(my_dict.get('Egor'))

print(my_dict.get('Oleg'))

my_dict.update({'Rim': 1968, 'Zoia': 1971})

print(my_dict.pop('Vasya'))

print(my_dict)

#-------------------------------
my_set = {1,1,3,3,4,5,6,True, 'Банан'}
print(my_set)

my_set.update([88, False])
my_set.discard(4)

print(my_set)