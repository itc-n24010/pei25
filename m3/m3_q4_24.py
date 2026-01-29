a = -100
b = 10

if a < 0 and b < 0 and a > b: #true and false and false
    c = a + b
    d = '有効な数字ではありません。'
elif (a < 0 and b < 0) or a > b:
    c = a / b
    d = '有効な数字ではありません。'
elif (a < 0 or b < 0) and a > b:
    c = a + b
    d = a > b
else:
    c = a / b
    d = a > b

print(f'{type(c)} {type(d)}')
