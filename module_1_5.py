immutable_var = 1, 2, 3, "String", "Book"
print('immutable tuple: ', immutable_var)
# immutable_var_1 = 1,2,3,4 # Ошибка типа: объект «кортеж»
# immutable_var_1[0][0] = 2 # не поддерживает назначение элементов
# print(immutable_var_1)
mutable_list = [[1, 2, 3, 4, 5], 0]
mutable_list[0][3] = "изменено"
print('Mutable list: ', mutable_list)
