from collections import deque
import sys
input = lambda : sys.stdin.readline().rstrip()

MAX = 100_001

n = int(input())
arr = list(map(int, input().split()))
arr.append(arr[-1])

cnt = [0]*MAX
result = 0

q = deque([])
for i in range(n+1):
    x = arr[i]
    cnt[x] += 1
    q.append(x)
    while cnt[x] > 1:
        result += len(q) - 1
        tmp = q.popleft()
        cnt[tmp] -= 1

print(result)
