a = '私はサッカーが好きです。'
b = 'サッカーはスポーツです。'

if 'サッカー' in a and 'バスケット' in b:
    print(a + b)
elif a.startswith('サッカー'):
    print(a.replace('サッカー', 'ゴルフ'))
elif b.find('は') == 4:
    print(b)
