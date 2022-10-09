# ЗАДАЧА 1
#  Реализуйте алгоритм задания 
# случайных чисел без использования 
# встроенного генератора псевдослучайных чисел.


# РЕШЕНИЕ 1
# x = input('Введите начальное число ')
# y = input('Введите конечное число ')
# import time
# t = str(time.time())[11:]
# while not(x<t<y):
#     t = t//2
# print(t)

# РЕШЕНИЕ 2
# import time
# print(str(time.time()).split('.')[_1])
# a = int(str(time.time()).split('.')[_1])
# start = int(input())
# end = int(input())
# print (a % (end - start) + start)

# ЗАДАЧА 2
# Задайте список. Напишите программу, которая определит, 
# присутствует ли в заданном списке строк некое число.

# РЕШЕНИЕ
# n = int(input('Введите искомое число '))
# x = int(input('Введите длину списка '))
# list = []
# for i in range (0, x):
#     list.append(input('Введите элемент списка '))
# print(list)
# for i in list[0, len(list)]:
#     if n in list[i]:
#         print(list[i])

# РЕШЕНИЕ 2
# some_list = [input() for _ in range(int(input('Введите кол-во элементов: ')))]
# n = int(input('Введите число: '))
# if str(n) in some_list:
#     print ('Да')
# else:
#     print ('нет')

# import time
# print(str(time.time()).split('.')[-1])
# a = int(str(time.time()).split('.')[-1])
# start = 50
# end = 1000
# print(a % (end - start) + start)

# РЕШЕНИЕ 3
# some_list = [input() for _ in range(int(input('Введите кол-во элементов: ')))]
# n = int(input('Введите число: '))
# if str(n) in some_list:
#     print('Да')
# else:
#     print('Нет')


# ЗАДАЧА 3
#  Напишите программу, которая определит 
# позицию второго вхождения строки в списке
# либо сообщит, что её нет.
# *Пример:*
# - список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
# - список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5
# - список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: -1
# - список: ["123", "234", 123, "567"], ищем: "123", ответ: -1
# - список: [], ищем: "123", ответ: -1

# РЕШЕНИЕ
# new_list = ["qwe", "asd", "zxc", "qwe", "ertqwe"]
# n = 'qwe'
# count = 0
# for i in range(0, len(new_list)):
#     if n == new_list[i]:
#         count = count+1
#         if count == 2:
#            print(i)
# if count < 2:
#     print (-1)

# РЕШЕНИЕ 2
# some_list = [input() for _ in range(int(input('Введите кол-во элементов: ')))]
# some_str = input('Введите строку: ')
# try:
#     print(some_list.index(some_str, some_list.index(some_str) + 1))
# except:
#     print(-1)

