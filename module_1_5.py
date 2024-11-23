immutable_var = (1, 2, 'a', 'b')
print(immutable_var)

# immutable_var [2] = 99
# print(immutable_var)             # ОШИБКА!!! т.к. мы пытаемся изменить элемент кортежа (неизменяемого типа данных)

mutable_list= [1,2,3, 'a', 'b', True]
mutable_list [5]= 999
print(mutable_list)
