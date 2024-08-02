immutable_var = 3, 5, True, 'apple'
print(immutable_var)
#immutable_var[3] = 'string'
#print(immutable_var)   Переменную нельзя изменить, потому что это кортеж а не строка

mutable_list = [4, 6, True, 'apple']
mutable_list[3] = 'string'
print(mutable_list)