import sys
input = lambda : sys.stdin.readline().rstrip()

n = int(input())
arr = []
for __ in range(n):
    a, b, c, d = map(int, input().split())
    am, bm = a*100+b, c*100+d
    if am < 301: am = 301
    if bm > 1201: bm = 1201
    arr.append((am, bm))
arr.sort()

cur = 301
m = 0
cnt = 0

for s, e in arr:
    if cur < s:
        cnt += 1
        cur = m
        m = 0
        if cur >= s:
            m = max(m, e)
        continue
    m = max(m, e)

if cur < 1201 and m:
    cur = m
    cnt += 1
print(cnt if cur >= 1201 else 0)
