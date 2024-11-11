def print_params(a=1, b='строка', c=True):
    print(a, b, c)


print_params(1, 25, [1, 2, 3])

values_list = [1, 'строка', 34]
values_dict = {'a': 1232, 'b': 3454, 'c': 'string'}
print_params(*values_list)
print_params(**values_dict)

values_list_2 = [54.32, 'Строка']
print_params(*values_list_2, 42)
