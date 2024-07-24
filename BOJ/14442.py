from collections import deque
import sys
input = lambda : sys.stdin.readline().rstrip()

n, m, k = map(int, input().split())
MAX = 999_999_999
arr = [list(input()) for __ in range(n)]
visited = [[[MAX]*(k+1) for __ in range(m)] for __ in range(n)]

visited[0][0][0] = 1
q = deque([(0, 0, 0)])
while q:
    x, y, w = q.popleft()
    if x == n-1 and y == m-1:
        continue

    for dx, dy in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
        nx, ny = x+dx, y+dy
        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue
        if arr[nx][ny] == '0':
            if visited[nx][ny][w] != MAX:
                continue
            q.append((nx, ny, w))
            visited[nx][ny][w] = min(visited[nx][ny][w], visited[x][y][w] + 1)
        else:
            if w+1 > k:
                continue
            if visited[nx][ny][w+1] != MAX:
                continue
            q.append((nx, ny, w+1))
            visited[nx][ny][w+1] = min(visited[nx][ny][w+1], visited[x][y][w] + 1)

ans = min(visited[-1][-1])
print(ans if ans != MAX else -1)
