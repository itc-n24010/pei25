list_e = [1, 2, 2, 7]
j = 0
for cd in [7, 3, 2, 6, 5]: #[7, 3, 2, 6, 5]から順に1つずつ取り出しcdに代入
    if cd in list_e: #list_eにcdが含まれていればTrue
        list_e.remove(cd) #cdと等しい最初の要素をlist_eから削除(１つだけ)
        list_e.insert(j, 2 * cd) #index j の位置に2倍した値を挿入(以降の要素は後ろにずれる)
        j += 1
print(list_e)

"""
(28)ループごとの変化
cd  j   list_e
7   0   [14, 1, 2, 2]
3   1   [14, 1, 2, 2]
2   1   [14, 4, 1, 2]
6       [14, 4, 1, 2]
5       [14, 4, 1, 2]
"""

result = ''
for e in [20, 6, -2, 12]:
    if (e + 4) ** 2 < 30: #(e+4)の2乗を表してる
        result += 'A'
    elif 4 < e / 3:
        result += 'B'
    else:
        result += 'C'
print(result)

"""
(29)ループごとのresultの内容
1回目：B
2回目：BC
3回目：BCA
4回目：BCAC
"""
