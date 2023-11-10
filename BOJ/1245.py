from collections import deque
import sys
input = lambda : sys.stdin.readline().rstrip()

dx = [0, 1, 0, -1, -1, 1, -1, 1]
dy = [1, 0, -1, 0, 1, -1, -1, 1]

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for __ in range(n)]
visited = [[0]*m for __ in range(n)]

def head(x, y):
    flag = 1
    visited[x][y] = 1
    q = deque([(x, y)])
    while q:
        x, y = q.popleft()
        for i in range(8):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if arr[x][y] < arr[nx][ny]:
                flag = 0
                continue
            if visited[nx][ny]:
                continue
            if arr[x][y] == arr[nx][ny]:
                visited[nx][ny] = 1
                q.append((nx, ny))
    return flag


cnt = 0
for i in range(n):
    for j in range(m):
        if visited[i][j]:
            continue
        if head(i, j):
            cnt += 1
print(cnt)
