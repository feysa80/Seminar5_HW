from random import random, randint


def first_player(pl1, pl2):
    pl = ''
    first_player = randint(1, 2)  # случайным образом выбираем кто будет ходить первым
    if first_player == 1:
        pl = pl1
    else:
        pl = pl2
    print(f'Первым ходит {pl}')
    return pl


def switch_pl(pl, pl1, pl2):
    if pl == pl1: pl = pl2
    else: pl = pl1
    return pl
