from collections import deque
import sys
input = lambda : sys.stdin.readline().rstrip()

n, m = map(int, input().split())
arr = [list(input()) for __ in range(n)]
visited = [[0]*51 for __ in range(51)]
q = deque([])
for i in range(n):
    for j in range(m):
        if arr[i][j] == 'S':
            q.append((0, i, j))
            visited[i][j] = 1
        if arr[i][j] == '*':
            q.appendleft((1, i, j))
            visited[i][j] = 1

while q:
    is_water, x, y = q.popleft()
    
    for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        nx, ny = x+dx, y+dy
        if not (0 <= nx < n and 0 <= ny < m):
            continue
        if visited[nx][ny]:
            continue
        if arr[nx][ny] == 'X':
            continue
        if arr[nx][ny] == 'D':
            if not is_water:
                print(visited[x][y])
                sys.exit()
            else:
                continue
        q.append((is_water, nx, ny))
        visited[nx][ny] = visited[x][y] + 1

print('KAKTUS')
