from collections import deque
import heapq
import sys
input = lambda : sys.stdin.readline().rstrip()
INF = int(1e9)

v, e = map(int, input().split())
graph = [[INF]*(v+1) for __ in range(v+1)]
for __ in range(e):
    a, b, c = map(int, input().split())
    graph[a][b] = c

for k in range(1, v+1):
    for i in range(1, v+1):
        for j in range(1, v+1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

ans = min([graph[i][i] for i in range(1, v+1)])
print(ans if ans != INF else -1)
