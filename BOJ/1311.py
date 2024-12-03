import sys
input = lambda : sys.stdin.readline().rstrip()

INF = int(1e9)

n = int(input())
arr = [list(map(int, input().split())) for __ in range(n)]
dp = [INF] * (2**21)

def solve(x, cnt):
    if x == n:
        return 0
    
    if dp[cnt] != INF:
        return dp[cnt]

    for i in range(n):
        if cnt & (2<<i):
            continue
        dp[cnt] = min(dp[cnt], solve(x+1, cnt | (2<<i)) + arr[x][i])
    
    return dp[cnt]

print(solve(0, 0))
