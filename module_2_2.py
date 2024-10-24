first = input('Введите число: ')
second = input('Введите чило: ')
third = input('Введите число: ')

if first == second and second == third:
    print(2)

elif first == second or second == third or first == third:
    print(first)
    print(second)
    print(third)

else:
    print(0)