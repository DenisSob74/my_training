students = {'Johnny', 'Bilbo', 'Steve', 'Kehndrick', 'Aaron'}
grades = []

students = sorted(students)
students_1 = students[0]
students_2 = students[1]
students_3 = students[2]
students_4 = students[3]
students_5 = students[4]

grades.append([5, 3, 3, 5, 4])
grades.append([2, 2, 2, 3])
grades.append([4, 5, 5, 2])
grades.append([4, 4, 3])
grades.append([5, 5, 5, 4, 5])

grades_1 = sum(grades[0]) / len(grades[0])
grades_2 = sum(grades[1]) / len(grades[1])
grades_3 = sum(grades[2]) / len(grades[2])
grades_4 = sum(grades[3]) / len(grades[3])
grades_5 = sum(grades[4]) / len(grades[4])

print(students_1, ':', grades_1, ',', students_2, ':', grades_2, ',', students_3, ':', grades_3, ',', students_4, ':', grades_4, ',', students_5, ':', grades_5)