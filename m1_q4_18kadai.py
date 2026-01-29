phrase = 'PythonProgramming'
list_p = []
for p in phrase:
    if p not in list_p:
        list_p.append(p)
print(len(phrase) - len(list_p))

for p in list_p:
    print(p, end="")
#list_p(すでに出てきた文字を記録しておく)の中身を１つずつ処理して、重複している文字があるかどうか確認したいから。

