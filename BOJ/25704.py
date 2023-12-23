a = int(input())
n = int(input())
dc = 0
if a >= 20:
    dc = max(dc, n * 0.25)
if a >= 15:
    dc = max(dc, 2000)
if a >= 10:
    dc = max(dc, n * 0.1)
if a >= 5:
    dc = max(dc, 500)
print(int(max(0, n - dc)))
