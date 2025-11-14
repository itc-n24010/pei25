list_a = ['Yokohama', 'Osaka', 'Nagoya', 'Sapporo', 'Fukuoka', 'Okinawa']
list_b = []
list_c = []
list_d = []
for name in list_a:
    if len(name) > 6:
        list_b.append(name)
    elif name.count('a') > 1:
        list_c.append(name)
    else:
        list_d.append(name)
print(f"list_bの内容：{list_b}")
print(f"list_cの内容：{list_c}")
print(f"list_dの内容：{list_d}")

