row = 3
sp = ' '
mark = '*'

for i in range(row):
    lr = sp * (row - i)
    center = mark * (i * 2 + 1)
    line = lr + center +lr
    print(line)
