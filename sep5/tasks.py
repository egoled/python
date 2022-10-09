# ЗАДАЧА 1
# Напишите программу, которая принимает на вход число N и выдаёт последовательность из N членов.
#     *Пример:*
#     - Для N = 5: 1, -3, 9, -27, 81

# РЕШЕНИЕ
# n = int(input('Введите N: '))
# for i in range (0, n-1):
#     print ((-3)**i, end = ', ')
# print ((-3)**(n-1))  


# ЗАДАЧА 2 
# Для натурального n создать словарь индекс-значение, состоящий из элементов последовательности 3n + 1.
#     *Пример:*
#     - Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

# РЕШЕНИЕ 1 (СО СЛОВАРЕМ)
# def func(x):
#     return 3 * x + 1

# n = int(input())
# some_dict = {}
# for i in range(1, n + 1):
#     some_dict[i] = func(i)
# print(some_dict)

# РЕШЕНИЕ 2 (СО СПИСКОМ)
n = int(input())
some_list = []
for i in range(n):
    some_list.append((-3) ** i)
print(*some_list, sep=', ')



# ЗАДАЧА 3
# Напишите программу, в которой пользователь будет задавать две строки, а программа - 
# определять количество вхождений одной строки в другой.

# РЕШЕНИЕ 1
# s1 = input('Введите первую строку: ')
# s2 = input('Введите вторую строку: ')
# if s1 > s2:
#    counter = s1.count(s2)
#    print(f'Количество вхождений {s1} в {s2} равно: ' + str(counter))
# else:
#     counter = s2.count(s1)
#     print(f'Количество вхождений {s2} в {s1} равно: ' + str(counter))

# РЕШЕНИЕ 2
# str1 = input()
# str2 = input()
# print(str1.lower().count(str2.lower()) or str2.lower().count(str1.lower()))


# РЕШЕНИЕ 3
# str1 = input()
# str2 = input()
# count = 0
# if len(str1) < len(str2):
#     len_str1 = len(str1)
#     i = 0
#     while i < len(str2):
#         if str1[0] == str2[i]:
#             if str1[1:] == str2[i + 1: i + len_str1]:
#                 count += 1
#                 i += len_str1
#             else:
#                 i += 1
#         else:
#             i += 1
# print(count)
