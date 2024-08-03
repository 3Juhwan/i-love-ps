import sys
input = lambda : sys.stdin.readline().rstrip()

MAX = 1_500_001
n = int(input())
arr = [list(map(int, input().split())) for __ in range(n)]
dp = [0] * (n + 1)

for i in range(n):
    dp[i] = max(dp[i], dp[i-1])
    if arr[i][0] + i <= n:
        dp[i + arr[i][0]] = max(dp[i + arr[i][0]], dp[i] + arr[i][1])

print(max(dp[-2], dp[-1]))
