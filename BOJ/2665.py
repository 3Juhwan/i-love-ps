from collections import deque
import sys
input = lambda : sys.stdin.readline().rstrip()

n = int(input())
arr = [list(map(int, list(input()))) for __ in range(n)]
visited = [[int(1e20)]*n for __ in range(n)]

q = deque([])
q.append((0, 0, 0)) if arr[0][0] else q.append((1, 0, 0))
if not arr[0][0]:
    visited[0][0] = 1

while q:
    w, x, y = q.popleft()
    if x==n-1 and y==n-1:
        continue
    if visited[x][y] < w:
        continue

    for dx, dy in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
        nx, ny = x+dx, y+dy
        if nx < 0 or nx >= n or ny < 0 or ny >= n:
            continue
        if visited[nx][ny] <= w:
            continue
        if arr[nx][ny]:
            visited[nx][ny] = w
            q.appendleft((w, nx, ny))
        else:
            visited[nx][ny] = w+1
            q.append((w+1, nx, ny))
    
print(visited[n-1][n-1])