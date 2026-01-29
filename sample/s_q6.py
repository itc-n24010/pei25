import random 
import sys #条件に合わない時にプログラムを強制終了する

# ('英単語', '日本語訳')をまとめているリスト
words = [('apple', 'りんご'), ('banana', 'バナナ'), 
         ('coconut', 'ココナッツ'), ('doughnut', 'ドーナツ'), 
         ('effort', '努力'), ('future', '未来'), ('gorilla', 'ゴリラ'), 
         ('house', '家'), ('information', '情報'), ('journey', '旅')]

questions = int(input('出題数を入力：')) #何問出すかユーザーに入力させる

length = len(words) #登録されている単語数を取得
if length < questions:
    print('登録された単語数以下の数値を入力してください。')
    sys.exit() #登録単語数より多い場合は即終了

count = 0 #何問目か
correct = 0 #正解数

while count < questions: #指定された問題数に達するまで繰り返す
    random.shuffle(words) #単語の順番はシャッフル
    ans_index = random.randint(0, 3)
    print(f'問題{count + 1}:{words[ans_index][0]}の意味は？')
    
    for i in range(2):
        print(f'{i * 2 + 1}:{words[i * 2][1]}, {i * 2 + 2}:{words[i * 2 + 1][1]}')
    answer = input('1から4の数字で解答（終了する場合は"x"を入力）：')
    if answer == 'x':
        break #xを入力したら途中で終了できる

    print(f'あなたの解答：{answer}')

    #正誤判定
    if answer == str(ans_index + 1):
        print('正解！')
        correct += 1
    else:
        print(f'不正解！正解は{ans_index + 1}の{words[ans_index][1]}でした！')

    count += 1 #問題数を進める
    
    #結果を出力
    print(f'成績：正解{correct}問 (全{count}問)')
