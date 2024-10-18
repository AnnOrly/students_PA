grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

# Посчитаем средний балл:

# Сумма оценок
a0 = sum(grades[0])
a1 = sum(grades[1])
a2 = sum(grades[2])
a3 = sum(grades[3])
a4 = sum(grades[4])

# Количество оценок
b0 = len(grades[0])
b1 = len(grades[1])
b2 = len(grades[2])
b3 = len(grades[3])
b4 = len(grades[4])

# Средний балл
point_average = [(a0 / b0), (a1 / b1), (a2 / b2), (a3 / b3), (a4 / b4)]
print(point_average)

# Перевод множества в список:
list_students = list(students)

# Сортировка списка учеников по алфавиту
alphabetically = list_students.sort()
print(list_students)

# Вывод словаря
students_PA = dict(zip(list_students, point_average))
print(students_PA)