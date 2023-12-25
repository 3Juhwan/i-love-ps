n, m = map(int, input().split())
ans = 0
for __ in range(n):
        a = input()
        if a.count("O") > m//2:
                ans += 1
print(ans)
