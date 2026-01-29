names = ['鈴木太郎', '田中花子']
print(names[-2])

list_a = [12,9,13,3,7,10]
list_b = []
for i in list_a: # 一つずつ取り出している
    list_b.append(int(i / 2 + 4))
print(f'私は{list_b[4]}歳です。') # int(3.5 + 4) = 7

month = 0
for i in list_a[-4:-2]: # スライスで後ろから4番目〜2番目手前までの要素[13,3]を取り出す
    month += int(i / 2) # iを2で割って小数点以下切り捨て 13/2→ 6，3/2→ 1,合計7となる

day = (list_a[2] + 30) // 2 # (13 + 30) // 2 → 21
print(f'{names[1]}の誕生日：{month}月{day}日')

list_c = []
for i in range(0, 12, 2): # 0から11まで2つずつ増加
    if i % 3 == 2: # iを3で割ったあまりが2のとき2,8
        list_c.pop() # listの末尾を削除
    else: #iを3で割ったあまりが2でない場合
        list_c.append(i) # 条件を満たさない値をリストの末尾に追加
print(f'{names[-1][-2:]}の誕生日：{list_c[0]}月{list_c[1]}日')

names.append(names[1][0:2] + names[0][2:]) #'田中' + '太郎'
names += ['小山田明子', '小森鈴太郎'] # ['鈴木太郎', '田中花子','田中太郎', '小山田明子', '小森鈴太郎']
total = 0
for s in names:
    if s.startswith('田'): # 先頭が'田'なら
        total += 1
    elif s.find('鈴') > 0: # '鈴'が先頭以外にある場合
        total += s.find('鈴') # '鈴'の位置（インデックス）をtotalに加算
    elif len(s) > 4: # 文字列が4文字よりも長い場合
        total += len(s) # totalに加算
print(total)

name = names[3][0:3] + names[1][2:]
month = 10
day = 13

print(f'{name}の誕生日：{month}月{day}日')

