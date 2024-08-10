# 1.Функция с параметрами по умолчанию:
def print_params(a=1, b='строка', c=True):
    print(a, b, c)


print_params()
print_params(0, 6)
print_params(22, 23, 25)

# Проверяем вызовы b = 25 и c = [1,2,3]
print_params(b=25)
print_params(c=[1, 2, 3])

# 2.Распаковка параметров:
values_list = [123, False, 'Вселенная']
values_dict = {'a': 42, 'b': 'world', 'c': [1, 2, 3]}

print_params(*values_list)
print_params(**values_dict)

# 3.Распаковка + отдельные параметры:
values_list_2 = [123.45, 'Ойкумена']
print_params(*values_list_2, 42)
