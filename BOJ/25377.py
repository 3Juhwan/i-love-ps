ans = int(1e9)
for __ in range(int(input())):
    a, b = map(int, input().split())
    if a > b:
        continue
    ans = min(ans, b)
print(ans if ans != int(1e9) else -1)
