from collections import deque
import sys
input = lambda : sys.stdin.readline().rstrip()

n = int(input())
arr = list(map(int, input().split()))
ans = [0]*(n+1)
for x in arr:
    ans[x] = ans[x-1] + 1
print(n-max(ans))
