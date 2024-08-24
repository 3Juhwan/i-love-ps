from collections import deque
import sys
input = lambda : sys.stdin.readline().rstrip()

MAX = 1000
v = [[[100000000000000000]*11 for __ in range(MAX)] for __ in range(MAX)]

n, m, k = map(int, input().split())
arr = [list(map(int, list(input()))) for __ in range(n)]

q = deque([(0, 0, k)])
v[0][0][k] = 1
dir = [(0, 1), (0, -1), (1, 0), (-1, 0)]
while q:
    x, y, limit = q.popleft()

    for dx, dy in dir:
        nx, ny = x+dx, y+dy
        if not (0 <= nx < n and 0 <= ny < m):
            continue
        if arr[nx][ny] == 0:
            if 1 + v[x][y][limit] < v[nx][ny][limit]:
                q.append((nx, ny, limit))
                v[nx][ny][limit] = 1 + v[x][y][limit]
            continue
        if arr[nx][ny] == 1 and limit:
            if v[x][y][limit] % 2:
                if 1 + v[x][y][limit] < v[nx][ny][limit-1]:
                    q.append((nx, ny, limit-1))
                    v[nx][ny][limit-1] = 1 + v[x][y][limit]
            else:
                if 2 + v[x][y][limit] < v[nx][ny][limit-1]:
                    q.append((nx, ny, limit-1))
                    v[nx][ny][limit-1] = 2 + v[x][y][limit]

ans = 100000000
for x in v[n-1][m-1]:
    if ans > x and x != 0:
        ans = x
print(ans if ans != 100000000 else -1)
