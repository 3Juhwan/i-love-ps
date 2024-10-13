import sys
input = lambda : sys.stdin.readline().rstrip()

n = int(input())
arr = [[]] + [list(map(int, input().split())) for __ in range(n)]

dp = [0] * (n+1)

for i in range(1, n+1):
    time, prev = arr[i][0], arr[i][2:]
    dp[i] = time + max([0]+[dp[x] for x in prev])
print(max(dp))
