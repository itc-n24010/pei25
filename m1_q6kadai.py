def search_kana_idx(kana):
    idx_1 = 0
    for gyou in hiragana_hyou:
        idx_2 = 0
        for ka in gyou:
            if ka == kana:
                return (idx_1, idx_2)
            else:
                idx_2 += 1
        idx_1 += 1
    return None

hiragana_hyou = [['あ', 'い', 'う', 'え', 'お'],
                 ['か', 'き', 'く', 'け', 'こ'],
                 ['さ', 'し', 'す', 'せ', 'そ'],
                 ['た', 'ち', 'つ', 'て', 'と'],
                 ['な', 'に', 'ぬ', 'ね', 'の'],
                 ['は', 'ひ', 'ふ', 'へ', 'ほ'],
                 ['ま', 'み', 'む', 'め', 'も'],
                 ['や', '゛', 'ゆ', '゜', 'よ'],
                 ['ら', 'り', 'る', 'れ', 'ろ'],
                 ['わ', 'っ', 'を', 'ー', 'ん']]

hirabun = input('ひらがなの文を入力してください：')
codes = ''
for kana in hirabun:
    idxs = search_kana_idx(kana)
    codes += '?' if idxs is None else f'{idxs[0]}{idxs[1]}'
print(codes)

ango = input('暗号を入力してください：')
kanas = ''
if len(ango) % 2 == 0:
    for i in range(len(ango) // 2):
        index_1 = int(ango[2 * i])
        index_2 = int(ango[2 * i + 1])
        kanas += '?' if index_2 > 4 else hiragana_hyou[index_1][index_2]
    print(kanas)
else:
    print('暗号の文字数は偶数でなければなりません。')
