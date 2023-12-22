a, b, c = map(int, input().split())
ans = 0
for i in range(c+1):
    if a >= i:
        ans = max(ans, min((a-i)//2, b-(c-i)))
print(ans)
