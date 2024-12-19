# ****** Лабораторная 2  Задание 1
students_dict = {
1: {'ФИО': 'Иванов Иван Иванович', 'возраст': 22, 'средний балл': 4.1},
2: {'ФИО': 'Петров Иван Степаныч', 'возраст': 23, 'средний балл': 4.5},
3: {'ФИО': 'Сидоров Сидор Сидорович', 'возраст': 26, 'средний балл': 3.8},
4: {'ФИО': 'Козлов Иван Петрович', 'возраст': 18, 'средний балл': 4.8},
5: {'ФИО': 'Николаев Алексей Николаевич', 'возраст': 22, 'средний балл': 4.3},
6: {'ФИО': 'Григорьев Андрей Григорьевич', 'возраст': 21, 'средний балл': 4.1},
7: {'ФИО': 'Александров Алексей Александрович', 'возраст': 25, 'средний балл': 4.0},
8: {'ФИО': 'Михайлов Степаныч Михайлович', 'возраст': 21, 'средний балл': 4.5},
9: {'ФИО': 'Егоров Егор Егорович', 'возраст': 22, 'средний балл': 4.2},
10: {'ФИО': 'Дмитриев Дмитрий Данилович', 'возраст': 21, 'средний балл': 4.1}
}

def find_students_by_age(students_dict, age):
 students_over_age = []
 for student_id in students_dict:
  if students_dict[student_id]['возраст'] > age:
   students_over_age.append(students_dict[student_id]['ФИО'])
 return students_over_age

age = 22
students_over_age = find_students_by_age(students_dict, age)
print(students_over_age)

#******** Задание 2
def uniq_num(lst):
 uniq_set = []
 for num in lst:
  if num not in uniq_set:
   uniq_set.append(num)
 return uniq_set

# Пример использования
numbers = [1, 2, 3, 1, 2, 4, 5]
result = uniq_num(numbers)
print(result)

#***** Задание 3
def sum_nat(n):

 if n == 0:
  return 0
 else:
  return n * (n + 1) / 2

n = 4
result = sum_nat(n)
print(f"Сумма первых {n} натуральных чисел равна: {result}")

#**** Задание 4
comm_num = lambda lst1, lst2: list(set(lst1) & set(lst2))

# Пример использования
lst1 = [1, 2, 3, 4, 5]
lst2 = [4, 5, 6, 7, 8]
result = comm_num(lst1, lst2)
print("Вывод лямбда функции")
print(result)