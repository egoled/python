# 1.Задайте строку из набора чисел. Напишите программу, которая покажет большее и меньшее число.
# В качестве символа – разделителя используйте пробел.
#



# some_list = [int[i] for i in input().split('')]
# print (min(some_list), max(some_list))

# a = [int[i] for i in input().split()]
# print(max(a), min(a))

# 2. Найдите корни квадратного уравнения Ax² + Bx + C = 0 двумя способами:
# 1) с помощью математических формул нахождения корней  квадратного уравнения
# 2) с помощью дополнительных библиотек Python
#

# import sympy as sm
# x = sm.Symbol('x')
# a = int(input())
# b = int(input())
# c = int(input())
# print(sm.solveset(a * x ** 2 + b * x + c, x))


# import math
# a = int(input())
# b = int(input())
# c = int(input())
#
# D = (b**2) - (4*a*c)
#
# if D < 0
#     print('корней нет')
#
# elif D == 0:
#     x = -b/2*a
# else:
#     x1 = (-b+math.sqrt(D))/(2*a)
#     x2 = (-b-math.sqrt(D))/(2*a)
#     print(round(x1, 2) round(x2, 2))
#
# # 3. Задайте два числа. Напишите программу, которая найдёт НОК(наименьшее общее кратное) этих двух чисел.
#
#
# x = int(input())
# y = int(input())
# if x > y:
#     greater = x
# else:
#     greater = y
# while(True):
#     if((greater % x == 0) and(greater % y == 0)):
#         lcm = greater
#         break
#         greater += 1
# print(lcm)