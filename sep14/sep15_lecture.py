# LAMBDA

# def f(x):
#     x**2
# g = f
# print (type(f))
# print(f(1))
# print(g(1))

# def f(x):
#     return x**2
# g = f
# print(type(f))
# print(g(4))

# def calc(x):
#     return x+10
# # print (calc(10))
#
# def calc2(x):
#     return x*10
# # print (calc2(10))
# #
# def math(op, x):
#     print(op(x))
# math (calc2, 10)

# def sum(x, y):
#     return x+y
#
# sum = lambda x, y: x+y+3
#
# def mult (x, y):
#     return x*y
#
# def calc (op, a, b):
#     print (op(a, b))
#     # return op(a, b)
#
# calc (lambda x, y: x+y, 4, 5)

# LIST COMPREHENSION
# list = []
# for i in range(1, 101):
#     # if(i%2 == 0):
#     list.append(i)
# print(list)

# list = [i for i in range(1, 21) if i % 2 == 0]

# def f(x):
#     return x**3
#
# list = [(i, f(i)) for i in range(1, 21) if i % 2 == 0]
# print(list)

# list = [1, 2, 3, 5, 8, 15, 23, 38]
#
# def q(x):
#     return x**2
#
# couples = [(i, q(i)) for i in range (1, len(list)) if i % 2 == 0]
# print(couples)

# f = open('f.txt', 'r')
# data = f.read() + ' '
# f.close()
# numbers = []
# while data != '':
#  space_pos = data.index(' ')
#  numbers.append(int(data[:space_pos]))
#  data = data[space_pos+1:]
# out = []
# for e in numbers:
#  if not e % 2:
#  out.append((e,e **2))
# print(out)
#
# def select (f, col):
#     return [f(x) for x in col]

# data = '1 2 3 5 8 15 23 38'.split()
# res = map(int, data)
# res = filter(lambda x: not x % 2, res)
# res = list(map(lambda x: (x, x**2), res))
# print(res)

# data = [x for x in range(10)]
# res = list(filter (lambda x: not x % 2, data))
# print(res)

# li = [x for x in range(1, 20)]
# li = list(map(lambda x: x+10, li))
# print(li)

# data = map(int, '23 67 98'.split())
# for e in data:
#     print(e)
# print('---')
# for e in data:
#     print(e)

# data = where(lambda e: not e % 2, data)
# data = list(select(lambda e: (e, e**2), data))
#
# def select(f, col):
#  return [f(x) for x in col]
# def where(f, col):
#  return [x for x in col if f(x)]
# data = '1 2 3 5 8 15 23 38'.split()
# data = select(int, data)
# data = where(lambda e: not e % 2, data)
# data = list(select(lambda e: (e, e**2), data))
#
# data = '1 2 3 5 8 15 23 38'.split()
# data = list(map(int, data))
# data = list(filter(lambda e: not e % 2, data))
# data = list(map(lambda e: (e, e**2), data))
# print(data)
#
# MAP
# f(x) ⇒ x + 10
# map(f, [ 1, 2, 3, 4, 5])
#
# FILTER
# f(x) ⇒ x - чётное
# filter(f, [ 1, 2, 3, 4,5])
#
# ZIP
# zip ([1, 2, 3], [ ‘о‘, ‘д‘, ‘т‘], [‘f’,’s’,’t’])
# [(1, 'о', 'f'), (2, 'д', 's'), (3, 'т', 't')]

users = ['user1', 'user2', 'user3', 'user4', 'user5']
ids = [4, 5, 9, 14, 7]
salary = [111, 222, 333]
data = list(enumerate(users))
print(data)



#
# ENUMERATE
# enumerate(['Казань', 'Смоленск', 'Рыбки', 'Чикаго'])
# [(0, 'Казань'), (1, 'Смоленск'), (2, 'Рыбки'), (3, 'Чикаго')]
