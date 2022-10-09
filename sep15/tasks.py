
products = ['iPad', 'Samsung Galaxy', 'iPhone', 'iRiver']

# list = filter(lambda x: x[0] == 'i', products)
# print(list)


# def isFirst(elem):
#     return elem[0] == "i"

# new_words1 = list(filter(lambda p: len(p) > 6, products))
# new_words2 = list(filter(lambda p: 'e' in p, products))
# print (new_words1)
# print (new_words2)
#
# def find_len(el):
#     return len(el) > 6

# prices = ['1578.4', '892.4', '354.1', '871.5']
#
# new_prices = tuple(map(float, prices))
# print(new_prices)


# my_str = 'nfnksm?/ikfwo/wfoi/'
# my_list = my_str.split('/')
# print(my_list)
#
# def my_func(*args):
#     for i in range(len(args)):
#       return i
#
# print (my_func(my_list))

# ЗАДАЧА
# применить скидку к товарам и округлить до 2 знака

DISCOUNT = 7
prices = ['1578.4', '892.4', '354.1', '871.5']

discounted_good = list(map(float, filter(lambda x:round(float(x)*(100 - DISCOUNT)/100, 2))))


str = input('Enter string: ').replace('абв', '').split(' ')
result = ' '.join(list(filter(lambda x: x != '', str)))
print(result)


# 35. Есть N натуральных чисел, записанных через пробел. Среди чисел не хватает одного, чтобы выполнялось условие A[i] - 1 == A[i-1]. Найдите это число.
# 	my_str = ‘1 2 3 5 6’ => 4
# 36. Дан список чисел. Создайте список, в который попадают числа, описываемые возрастающую последовательность. Порядок элементов менять нельзя.
# Пример:
# [1, 5, 2, 3, 4, 6, 1, 7] => [1, 5, 6, 7]
#
# 37. Напишите программу, удаляющую из текста все слова, содержащие "абв".
