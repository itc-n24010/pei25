a = 2 #aに2を代入する
numbers = [] #結果を入れるための空のリストを用意する

for i in range(6): #6回繰り返して6つ要素を作る
    numbers.append(a) #appendメソッドで、aの値をリストnumbersの末尾に1つ追加する
    a = a * 2 #次の値を作るため2倍する

print(numbers)

