n = int(input("Введите число от 3 до 20: "))

if n < 3 or n > 20:
    print("Число вне допустимого диапазона!")

else:
    result = ""

    for i in range(1, n):
        for j in range(i + 1, n):

            if n % (i + j) == 0:
                result += f'({i}{j})'

    print(f"Пары чисел для числа {n}, чтобы оно делилось на их сумму без остатка: {result}")


