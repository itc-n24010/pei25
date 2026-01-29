def check_num(num):
    a = num[1]
    b = num[-1]
    c = len(num) == 919
    d = len(num) > 0

    print(f'aの値のtype: {type(a)}')
    print(f'bの値のtype: {type(b)}')
    print(f'cの値のtype: {type(c)}')
    print(f'dの値のtype: {type(d)}')

    if a == b and c and d:
        print(a * b)
    elif a == b or c or d:
        print(b * 2)

num = '919'
check_num(num)
