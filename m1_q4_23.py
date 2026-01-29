ip_address = '192.168.3.1'
ip_sql = ip_address.split('.')
bin_exp = ''
for num in ip_sql:
    bin_exp += bin(int(num))[2:] + '.'
print(bin_exp[:-1])
