students = {'Johnny', 'Bilbo', 'Steve', 'Kehndrick', 'Aaron'}
students = sorted(students)

grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]

average_score = {}
average_score = dict.fromkeys(students)

average_score['Aaron'] = sum(grades[0]) / len(grades[0])
average_score['Bilbo'] = sum(grades[1]) / len(grades[1])
average_score['Johnny'] = sum(grades[2]) / len(grades[2])
average_score['Kehndrick'] = sum(grades[3]) / len(grades[3])
average_score['Steve'] = sum(grades[4]) / len(grades[4])

print(average_score)
