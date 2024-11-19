numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primers = []
not_primers = []
for index in range(len(numbers)):
    is_prime = True
    for divider in range(2, numbers[index]):
        if numbers[index] % divider == 0:
            is_prime = False
    if numbers[index] > 1:
        if is_prime == True:
            primers.append(numbers[index])
        else:
            not_primers.append(numbers[index])

print('primers = ', primers)
print('not_primers =', not_primers)

