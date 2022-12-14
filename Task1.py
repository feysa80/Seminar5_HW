from random import random, randint
bonbons = 100 #количество конфет
index = 28 #максимальное кол-во кофет за ход
win = bonbons % (index+1) #выигрышная комбинация для первого хода
player1 = input('Введите ваше имя: ')
player2 = 'бот'
player = ''
first_player = randint(1, 2) #случайным образом выбираем кто будет ходить первым
if first_player == 1: player = player1
else: player = player2
print(f'Первым ходит {player}')


def check(x, b, c):#Проверка кол-ва конфет, которое берёт игрок
    #x - сколько взял игрок, b- максимальное кол-во, которое он может взять, с-сколько всего есть конфет
    if 1 <= x <= b and x <= c: return x
    elif 1 <= x <= b and x > c:
        while not (1 <= x <= b and x <= c):
            x = int(input(f'Осталось всего {c} конфет(ы). Введите число от 1 до {c} включительно: '))
    else:
        while not(1 <= x <= b):
            x = int(input(f'Вы неправильно ввели кол-во конфет. Введите число от 1 до {x} включительно: '))
    return x


def game(k, x, pl1, pl2):
    # k - кол-во конфет, х - максимум который можно взять, pl1 - игрок1, pl2 -игрок2(бот)
    while k > 0:
        pl = pl1
        print(f'Осталось {k} конфет(ы). Вы можете взять от 1 до {x} конфет')
        taken = int(input('Ваш ход: '))
        taken = check(taken, x, k)
        k -= taken
        if k == 0:
            break
        pl = pl2
        print(f'Осталось {k} конфет(ы). Теперь ходит {pl}')
        if k % (x + 1) != 0:
            taken = k % (x + 1)
        else:
            taken = randint(1, 28)
        k -= taken
        print(f'{pl} взял {taken} конфет')
    print(f'Всё! Конфеты закончились! Победил {pl}')


if player == player2:
    print(f'Бот взял {win} конфет')
    bonbons = bonbons - win
    player = player1
    # print(f'Осталось {bonbons} конфет. Вы можете взать от 1 до 28 конфет')
    # taken = input('Ваш ход: ')
    game(bonbons, index, player1, player2)
else:
    game(bonbons, index, player1, player2)











