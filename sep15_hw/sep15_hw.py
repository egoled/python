# ЗАДАЧА 1
# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".
#

# РЕШЕНИЕ
# data = 'абвиняемая была очень абворожительна'
# print(data)
# data = list(filter(lambda e: 'абв' not in e, data.split(' ')))
# new_data = (' '.join(data))
# print(new_data)



# ЗАДАЧА 2
# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход.
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""
#

#ВАРИАНТ НА 2 ИГРОКА
# welcome_text = ('На столе лежит 2021 конфета. Играют два игрока, делая ход друг после друга.\n'
# 'Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.\n'
# 'Все конфеты оппонента достаются сделавшему последний ход.')
# print(welcome_text)
#
# from random import randint
#
# def take_step(name):
#     x = int(input(f"{name}, Сколько возьмете конфет в этот ход? => "))
#     while x < 1 or x > 28:
#         x = int(input(f"{name}, можно брать от 1 до 28: "))
#     return x
#
# def step_made (name, k, counter, all_candies):
#     print(f"{name} забирает за этот ход {k} конфет и доводит их общее число у себя до {counter}. На столе осталось {all_candies} конфет.")
#
# player1 = input("Введите имя первого игрока: ")
# player2 = input("Введите имя второго игрока: ")
# all_candies = 2021
# counter1 = 0
# counter2 = 0
#
# turn = randint(0,1)
# if turn:
#     print(f"{player1}, ваш ход первый!")
# else:
#     print(f"{player2}, ваш ход первый!")
#
# while all_candies > 28:
#     if turn:
#         k = take_step(player1)
#         counter1 += k
#         all_candies -= k
#         turn = False
#         step_made(player1, k, counter1, all_candies)
#     else:
#         k = take_step(player2)
#         counter2 += k
#         all_candies -= k
#         turn = True
#         step_made(player2, k, counter2, all_candies)
# if turn:
#     print(f"{player1} побеждает!")
# else:
#     print(f"{player2} побеждает!")


#ВАРИАНТ ИГРОК ПРОТИВ БОТА
# welcome_text = ('На столе лежит 2021 конфета. Вы играете против бота, делая ход друг после друга.\n'
# 'Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.\n'
# 'Все конфеты оппонента достаются сделавшему последний ход.')
# print(welcome_text)
#
# from random import randint
#
# def take_step(name):
#     x = int(input(f"{name}, Сколько возьмете конфет в этот ход? => "))
#     while x < 1 or x > 28:
#         x = int(input(f"{name}, можно брать от 1 до 28: "))
#     return x
#
# def step_made (name, k, counter, all_candies):
#     print(f"{name} забирает за этот ход {k} конфет и доводит их общее число у себя до {counter}. На столе осталось {all_candies} конфет.")
#
# player1 = input("Введите имя первого игрока: ")
# player2 = 'Бот'
# all_candies = 2021
# counter1 = 0
# counter2 = 0
#
# turn = randint(0,1)
# if turn:
#     print(f"{player1}, ваш ход первый!")
# else:
#     print(f"{player2} ходит первым")
#
# while all_candies > 28:
#     if turn:
#         k = take_step(player1)
#         counter1 += k
#         all_candies -= k
#         turn = False
#         step_made(player1, k, counter1, all_candies)
#     else:
#         k = randint(1, 28)
#         counter2 += k
#         all_candies -= k
#         turn = True
#         step_made(player2, k, counter2, all_candies)
#
# if turn:
#     print(f"{player1} побеждает!")
# else:
#     print(f"{player2} побеждает!")


# ЗАДАЧА 3
# Создайте программу для игры в ""Крестики-нолики"".
#
board = list(range(1,10))

# def create_board(board):
#     print('-'*12)
#     for i in range(3):
#         print('|', board[0+i*3],'|', board[1+i*3], '|', board[2+i*3], '|')
#         print('-'*12)
# def choice(tic_tac):
#     valid = False
#     while not valid:
#         player_index = input('Ваш ход, выберите ячейку ' + tic_tac + ' --> ')
#         try:
#             player_index =int(player_index)
#         except:
#             print('Не туда')
#             continue
#         if player_index >= 1 and player_index <= 9:
#             if(str(board[player_index-1]) not in 'XO'):
#                 board[player_index-1] = tic_tac
#                 valid = True
#             else:
#                 print('Занято')
#         else:
#             print('Еще раз попробуй')
#
# def victory_check(board):
#     victory = ((0,1,2),(3,4,5),(6,7,8),
#                (0,3,6),(1,4,7),(2,5,8),
#                (0,4,8),(2,4,6))
#     for i in victory:
#         if board[i[0]] == board[i[1]] == board[i[2]]:
#             return board[i[0]]
#     return False
#
# def game(board):
#     counter =0
#     vic = False
#     while not vic:
#         create_board(board)
#         if counter % 2 == 0:
#             choice('X')
#         else:
#             choice('0')
#         counter +=1
#         if counter > 4:
#             tt_win = victory_check(board)
#             if tt_win:
#                 print(tt_win,'Победа')
#                 vic = True
#                 break
#             if counter == 9:
#                 print('Ничья)')
#         create_board(board)
# game(board)

# ЗАДАЧА 4
# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

# with open('original_text.txt', 'r') as data:
#     my_text = data.read()
#
# def encode(ss):
#     str_code = ''
#     prev_char = ''
#     count = 1
#     for char in ss:
#         if char != prev_char:
#             if prev_char:
#                 str_code += str(count) + prev_char
#             count = 1
#             prev_char = char
#         else:
#             count += 1
#     return str_code
#
# str_encode = encode(my_text)
# print(str_encode)
#
# with open('compressed_text.txt', 'w', encoding='UTF-8') as data:
#     encoded = data.write(str_encode)
#
# with open('compressed_text.txt', 'r') as data:
#     my_text2 = data.read()
#
#
# def decode(ss:str):
#     count = ''
#     str_decode = ''
#     for char in ss:
#         if char.isdigit():
#             count += char
#         else:
#             str_decode += char * int(count)
#             count = ''
#     return str_decode
#
# str_decode = decode(my_text2)
# print(str_decode)