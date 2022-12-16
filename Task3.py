string_in = input('Введите строку: ')


def convert_rle(str):
    elem = string_in[0]
    count = 0
    res1 = []
    res2 = []
    for i in string_in:
        if i == elem:
            count += 1
        else:
            res1.append(elem)
            res2.append(count)
            elem = i
            count = 1
    res1.append(elem)
    res2.append(count)
    res = list(zip(res1, res2))
    return res


def reconvert_rle(lst):
    res1, res2 = zip(*lst)
    temp = list(map(lambda x,y: x*y, res2, res1))
    res = ''.join(temp)
    return res


str_new = convert_rle(string_in)
print(str_new)
print(reconvert_rle(str_new))
