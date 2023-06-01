
# n1 = 22                     #глобальная переменная
#
# def f1():
#     n1=0
#     print(n1)
#     pass
#
# def f2(x):
#     n3=11
#    # global n1               #разрешение менять глобальную функцию
#     x+=100
#     print(x)
#     pass
#
# f1()
# f2(n1)
#
# def f3(x):
#     r = x+12
#     return r
# result = f3(100)
# print(result)

# for     повторяет Н раз
# while   повторяет пока проверка верна
# n = 100
# for i in range(10):
#     n+=1
#     print(n)
#     pass
#
# while n<120:
#     n+=1
#     print(n)
#     pass

# bash = 10
# for i in range(10):
#     bash+=2.5
#     result = bash
# print(f'Высота башни {result} метров')
#
# bash = 10
# day = 0
# while bash<150:
#     bash += 2.5
#     day+=1
#     result = bash
# print(f'дней нужно {day}')

#[1,2,3] list массив обычный
#(1,2,3) tuple не изменяемый массив
#{'name':'Alex','age':'56'} dict словарь
#set () уникальный набор элементов

# mas = ['cat','dog','pig','cow','duck','chiken','bear']
# print(len(mas))
#
# students = ['Alex','Jo','Ben','Li','Bo']
# print((students[0]))
# print((students[1]))
# print((students[2]))
# print((students[3]))
# print((students[4]))
# for i in range(len(students)):
#     print(students[i])
# print('########################')
# for s in students:
#     print(s)
# print('########################')
# k=0
# # while k<len(students):
# #     print(students[k])
# #     k+=1
# print('########################')
# while True:
#     print(students[k])
#     k+=1
#     if k==len(students):
#         break
# print('########################')
# for i in mas:
#     print(i, 'уснул')
# print('########################')
# import random
# n = random.randint(1,5)
#
# print(n)
# from random import randint
# import random as r
# n = 0
# while True:
#     n = random.randint(1,100)
#     print(n)
#     if n == 33:
#         break

# croco = 0
# meat = 0
# while True:
#     meat += random.randint(1,5)
#     croco+=meat
#     print(croco)
#     print('наелся')
#     if croco < 25:
#         break
# def cat():
#     print('^--&^')
#     print('=0.0=')
#     print('u   u')
#     pass
#
# def text(t):
#     print('*******',t,'**********')
#     pass
# import random
# def kubik():
#     n = random.randint(1, 6)
#
# kubik()
#
# n = int(input('введи число\n'))
# if n %2==0:
#     print('четное число')
# if n%2==1:
#     print('нечетное число')
# import random
# a = int(input('введи число до 100\n'))
# b = 0
# c = 0
# for i in range(a):
#     ran = random.randint(1, 100)
#     print(ran)
#     if ran%2==0:
#         b+=ran
#     else:
#         c+=ran
# print(f'сумма четных {b}')
# print(f'сумма нечетных {c}')

# Задание 1
for i in range(1, 11):
    for j in range(1, 11):
        result = i * j
        print(f"{i} * {j} = {result}", end=" ")

    print()

#Задание 2
import random

def roll():
    return random.randint(1, 6)

def game():
    player1_game = 0
    player2_game = 0

    while True:
        player1_roll1 = roll()
        player1_roll2 = roll()
        print('Игрок 1:')
        print(f'***************     ***************')
        print(f'**           **     **           **')
        print(f'**     {player1_roll1}     **     **     {player1_roll2}     **')
        print(f'**           **     **           **')
        print(f'***************     ***************')

        if player1_roll1 == player1_roll2:
            player1_game = player1_roll1 + player1_roll2
            break

    while True:
        player2_roll1 = roll()
        player2_roll2 = roll()
        print('Игрок 2:')
        print(f'***************     ***************')
        print(f'**           **     **           **')
        print(f'**     {player2_roll1}     **     **     {player2_roll2}     **')
        print(f'**           **     **           **')
        print(f'***************     ***************')

        if player2_roll1 == player2_roll2:
            player2_game = player2_roll1 + player2_roll2
            break

    if player1_game > player2_game:
        print("Игрок 1 победил!")
    elif player2_game > player1_game:
        print("Игрок 2 победил!")
    else:
        print("Ничья!")
game()







