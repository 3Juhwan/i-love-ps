import sys
input = lambda : sys.stdin.readline().rstrip()

n = int(input())
arr = [list(map(int, input().split())) for __ in range(n)]
ans = 0

def solve(idx, cnt):
    global ans

    if ans >= cnt + 2*(n - idx):
        return 

    if idx == n:
        ans = max(ans, cnt)
        return

    if arr[idx][0] <= 0:
        solve(idx + 1, cnt)
        return

    f = 1
    for i in range(n):
        if i != idx and arr[i][0] > 0:
            conflict(i, idx)
            solve(idx + 1, cnt + (1 if arr[i][0] <= 0 else 0) + (1 if arr[idx][0] <= 0 else 0))
            rollback(i, idx)
            f = 0
    if f:
        solve(idx + 1, cnt)

def conflict(a, b):
    w1, h1 = arr[a]
    w2, h2 = arr[b]
    arr[a][0] -= h2
    arr[b][0] -= h1

def rollback(a, b):
    w1, h1 = arr[a]
    w2, h2 = arr[b]
    arr[a][0] += h2
    arr[b][0] += h1

solve(0, 0)

print(ans)
