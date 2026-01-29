name_a = 'ant'
name_b = 'Attention please'
strs = ''
for b in name_b:
    if name_a.find(b) >= 0:
        strs += b
print(strs)
