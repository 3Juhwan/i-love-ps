from collections import deque
import sys
input = lambda : sys.stdin.readline().rstrip()

dir = {
    0: (-1, 0),
    1: (0, 1),
    2: (1, 0),
    3: (0, -1)
}
INF = 999_999_999_999
m, n = map(int, input().split())
arr = [list(input()) for __ in range(n)]
v = [[[INF]*4 for __ in range(m)] for __ in range(n)]
q = deque([])
for i in range(n):
    for j in range(m):
        if arr[i][j] == 'C' and not q:
            arr[i][j] = '.'
            for k in range(4):
                nx, ny = i+dir[k][0], j+dir[k][1]
                if not (0 <= nx < n and 0 <= ny < m):
                    continue
                if arr[nx][ny] == '*':
                    continue
                v[nx][ny][k] = 0
                q.append((nx, ny, k, 0))
ans = INF
cnt = 0
while q:
    x, y, d, w = q.popleft()
    if arr[x][y] == 'C':
        ans = min(ans, w)
        continue
    if v[x][y][d] != w:
        continue
    cnt += 1
    for i in range(4):
        if (d+2) % 4 == i:
            continue
        nx, ny = x+dir[i][0], y+dir[i][1]
        if not (0 <= nx < n and 0 <= ny < m):
            continue
        if arr[nx][ny] == '*':
            continue
        c = w if d==i else w+1
        if v[nx][ny][i] <= c:
            continue
        q.append((nx, ny, i, c))
        v[nx][ny][i] = c

print(ans)
