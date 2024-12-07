def print_params(a=1, b='строка', c=True):
    print(a, b, c)
    return


print_params()
print_params(b=25)
print_params(c = [1,2,3])

values_list = ['Job', False, 1]
values_dict = {'a':'Job', 'b':False, 'c':1}


print_params(*values_list)
print_params(**values_dict)

values_list_2 = (True, "True")
print_params(*values_list_2, 42)