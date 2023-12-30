paper = {136: 1_000, 142: 5_000, 148: 10_000, 154: 50_000}
ans = 0
for __ in range(int(input())):
    a, b = map(int, input().split())
    ans += paper[a]
        break
print(ans)
