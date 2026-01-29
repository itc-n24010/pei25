'''
①
・比較演算子'=='
値が等しいかを比較する
オブジェクトの「中身」が同じならTrue
例)
a = [1, 2, 3]
b = [1, 2, 3]
print(a == b)  # True（中身が同じ）

・'is'
同じオブジェクトか(メモリ上で同一か)を比較する
id(a) == id(b)と同じ意味
例)
print(a is b)  # False（別のオブジェクト）
'''

#②
a = [1, 2, 3]
b = a

print(a is b)        # True
print(bool(a is b)) # True

