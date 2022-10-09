# Задача HARD SORT.
# Задайте двумерный массив из целых чисел.
# Количество строк и столбцов задается с клавиатуры.
# Отсортировать элементы по возрастанию слева направо и сверху вниз.
# Например, задан массив:
# 1 4 7 2
# 5 9 10 3
# После сортировки
# 1 2 3 4
# 5 7 9 10

# import random as r
# rows = int(input('Число строк в массиве '))
# columns  = int(input('Число колонок в массиве '))
# matrix = [[r.randint(-10, 10) for i in range(columns)] for j in range(rows)]
# temp = []
# for i in range (rows):
#     for j in range (columns):
#         temp.append(matrix[i][j])
#
# def sort(arr):
#     min = arr[0]
#     # max = arr[0]
#     # for k in range (len(arr)//2):
#         for i in range (k, len(arr)-k):
#              if arr[i]>[max]:
#                   max = i
#              if arr[i]<min:
#                   min = i
#         arr[min], arr[k],  arr[max], arr[len(arr) - 1 - k] = arr[k], arr[min], arr[len(arr) - 1 - k], arr[max]
#     return arr
#
# for i in range (rows):
#     for j in range (columns):
#         matrix[i][j] = temp[i+j]
# print(matrix)
#
# for element in matrix:
#     element.sort()
# print(matrix)
#
# задача 2 HARD необязательная. Сгенерировать массив
# случайных целых чисел размерностью m*n (размерность вводим с клавиатуры).
# Вывести на экран красивенько таблицей.
# Перемешать случайным образом элементы массива, причем чтобы каждый гарантированно один раз переместился на другое место и потом не участвовал никак (возможно для этого удобно будет использование множества) и выполнить это за m*n / 2 итераций. То есть если массив три на четыре, то надо выполнить не более 6 итераций. И далее в конце опять вывести на экран как таблицу.

# from random import randint
# from random import choice
#
# n = int(input("Insert n: "))
# m = int(input("Insert m: "))
#
# initList = []
# tempList = []
#
# for i in range(n):
#     sp = []
#     for j in range(m):
#         sp.append(randint(-10, 10))
#         tempList.append(sp[j])
#     initList.append(sp)
# print(initList)
# print(tempList)
# indexList = [0] * m*n
# for i in range(m*n):
#     indexList[i] = i
#
# for i in range(int(m*n/2)):
#     a = choice(indexList)
#     indexList.remove(a)
#     b = choice(indexList)
#     indexList.remove(b)
#     tempList[a], tempList[b] = tempList[b], tempList[a]
# resultList = []
# print(tempList)
# for i in range(n):
#     sp = []
#     for j in range(m):
#         sp.append(tempList[0])
#         tempList.remove(tempList[0])
#     resultList.append(sp)
#
# print(resultList)

# 1.# Напишите программу вычисления арифметического выражения
# заданного строкой.Используйте операции +, -, /, *.приоритет
# операций стандартный.
# *Пример: *
# 2 + 2 = > 4;
# 1 + 2 * 3 = > 7;
# 1 - 2 * 3 = > -5;
# - Добавьте возможность использования
# скобок, меняющих приоритет операций.
#
# *Пример: *
# 1 + 2 * 3 = > 7;
# (1 + 2) * 3 = > 9;
# 43. Дана последовательность чисел.Получить список
# уникальных элементов заданной последовательности.
# *Пример: *
# [1, 2, 3, 5, 1, 5, 3, 10] = > [2, 10]

some_string = '5+4*6/12'
list_of_op = ['-', '+', '*', '/']

def split_into_afrin (some_string, list_of_op):
    positions = []
    operator = []
    numbers = []
    temp = ''
    for char in some_string:
        if not char is list_of_op:
            temp+=char
        else:
            operator.append(char)
            numbers.append(int(temp))
            temp = ''
    numbers.append(int(temp))
    print(numbers)
    print(operator)

    while len(numbers)>1:
        if '*' in operator:
            index = operator.index('*')
            temp = parser (numbers[index], numbers[index+1], '*')
            numbers[index] = temp
        elif '/' in operator:
            index = operator.index('/')
            temp = parser (numbers[index], numbers[index+1], '/')
            numbers[index] = temp
        elif '+' in operator:
            index = operator.index('+')
            temp = parser (numbers[index], numbers[index+1], '+')
            numbers[index] = temp
        elif '-' in operator:
            index = operator.index('-')
            temp = parser (numbers[index], numbers[index+1], '-')
            numbers[index] = temp

        del(numbers[index+1])
        del(operator[index])

def parser (num1, num2, operator)
    if operator == '+':
        return num1+num2
    if operator == '*':
        return num1*num2
    if operator == '-':
        return num1-num2
    if operator == '/':
        return num1/num2


    # for index in range(len(some_string)):
    #     if some_string[index] in list_of_op:
    #         positions.append(index)
    # numbers = [int(some_string[0:positions[0]])]
    # for i in positions:
    #     numbers.append(some_string[])





