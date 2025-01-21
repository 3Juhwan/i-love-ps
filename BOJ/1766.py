from collections import deque
import math
import heapq
import sys
sys.setrecursionlimit(10101)
input = lambda : sys.stdin.readline().rstrip()
INF = int(1e9)
MAX = 1_000_001
MOD = 1_000_000_003

n, m = map(int, input().split())
dep = [[] for __ in range(n+1)]
cnt = [0]*(n+1)
for __ in range(m):
    a, b = map(int, input().split())
    dep[a].append(b)
    cnt[b] += 1

q = []
for i in range(1, n+1):
    if cnt[i] == 0:
        heapq.heappush(q, i)
while q:
    x = heapq.heappop(q)
    print(x, end=' ')
    for i in sorted(dep[x]):
        cnt[i] -= 1
        if cnt[i] == 0:
            heapq.heappush(q, i)
