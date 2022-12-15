import functions as f
print('Игра в крестики и нолики')
player1 = input('Введите имя первого игрока: ')
player2 = input('Введите имя второго игрока: ')
player = f.first_player(player1, player2)
symbol1 = 'X'
symbol2 = '0'
symbol = symbol1
desk = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]
desk1 = []
desk2 = []
desk_pl = [desk1, desk2]
win = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9'], ['1', '4', '7'], ['2', '5', '8'], ['3', '6', '9'],
       ['1', '5', '9'], ['3', '5', '7']]
count = 1
result = False


def print_desk(dsk):
    for i in dsk:
        print(*i, sep=' | ')


def turn(dsk, num, symb):
    count = 0
    if int(num) < 1 or int(num) > 9:
        num = input(f'Вы неверно ввели номер, введите свободный номер от 1 до 28 включительно: ')
        turn(dsk, num, symb)
    for i in range(len(dsk)):
        if dsk[i].__contains__(num):
            temp = " ".join(dsk[i])
            temp = temp.replace(num, symb)
            dsk[i] = temp.split()
            count +=1
    if count == 0:
        num = input(f'Клетка №{num} уже занята, введите другой номер: ')
        turn(dsk, num, symb)
    return dsk


def check_win(lst1, lst2):
    res = False
    lst = set(lst1).intersection(set(lst2))
    if len(lst) == 3:
        res = True
    return res


while not result:
    for i in range(2):
        print_desk(desk)
        current_turn = input(f'{player} ходит "{symbol}"-ми, введите номер клетки: ')
        desk = turn(desk, current_turn, symbol)
        desk_pl[i].append(current_turn)
        count += 1
        for item in win:
            if check_win(desk_pl[i], item):
                result = True
                break
        if result:
            break
        if count > 8:
            break
        player = f.switch_pl(player, player1, player2)
        symbol = f.switch_pl(symbol, symbol1, symbol2)
    if count > 8:
        break
print_desk(desk)
if result:
    print(f'{player} победил!')
else:
    print('Ничья!!!')




