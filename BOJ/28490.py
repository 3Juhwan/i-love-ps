ans = 0
for __ in range(int(input())):
    a, b = map(int, input().split())
    ans = max(ans, a * b)
print(ans)
