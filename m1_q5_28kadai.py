day = ['月','月','火','水','木','金','金']
a = 0

for x in ['月','火','水','木','金','土','日']:
    while x in day: #dayにその曜日が含まれていたら処理
        day.remove(x) #重複している曜日を１つ削除
    day.insert(a, x) #正しい順で先頭側に挿入
    a += 1

print(day) 
