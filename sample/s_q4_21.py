numbers = [1, 2, 3, 4, 5]
ans = 0
for n in numbers:
    if n % 2 == 0:
        ans += n
ans *= 2
print(ans)
