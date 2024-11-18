def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)
print_params(50, 25)
print_params(50, 25, "Hello")
print_params(80)
print_params()
print_params(b = 25)
print_params(c = [1,2,3])

values_list = [60, "Дерево", True]
values_dict = {'a' : 150, 'b' : 'Колесо', 'c' : False }
print_params(*values_list,)
print_params(**values_dict)
values_list_2 = [199, "Муха"]
print_params(*values_list_2, 42)