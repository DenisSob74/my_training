numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primers = []
not_primers = []
for number in range(2, len(numbers) + 1):
    index = 0
    for is_prime in range(1, number + 1):
        if number % is_prime == 0:
            index += 1
    if index == 2:
        primers.append(is_prime)
    else:
        not_primers.append(is_prime)

print('primers = ', primers)
print('not_primers =', not_primers)