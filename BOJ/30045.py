cnt = 0
for __ in range(int(input())):
    a = input()
    cnt += 1 if 'OI' in a or '01' in a else 0
print(cnt)
