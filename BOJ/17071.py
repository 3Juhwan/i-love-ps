from collections import deque
import sys
input = lambda : sys.stdin.readline().rstrip()

MAX = 500_000
n, k = map(int, input().split())
if n == k:
    print(0)
    sys.exit()

visited = [[0]*2 for __ in range(MAX+1)]
q = deque([n])
for i in range(1, MAX+1):
    next_q = deque([])
    while q:
        x = q.popleft()
        for dx in [-1, 1, x]:
            nx = x + dx
            if nx > MAX or nx < 0:
                continue
            if visited[nx][i%2]:
                continue
            visited[nx][i%2] = 1
            next_q.append(nx)
    k += i
    
    if k <= MAX and visited[k][i%2]:
        print(i)
        break
    q = next_q
else:
    print(-1)
