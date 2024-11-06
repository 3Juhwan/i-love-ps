from collections import deque
import sys
input = lambda : sys.stdin.readline().rstrip()
INF = int(1e9)

n, m, t = map(int, input().split())
arr = [list(map(int, input().split())) for __ in range(n)]

def move_clock_wise(x, k):
    k %= m
    for i in range(n):
        if (i+1) % x == 0:
            arr[i] = arr[i][-k:] + arr[i][:-k]

def move_counter_clock_wise(x, k):
    k %= m
    for i in range(n):
        if (i+1) % x == 0:
            arr[i] = arr[i][k:] + arr[i][:k]

def bfs(visited, x, y):
    global arr

    ans = []
    q = deque([(x, y)])
    visited[x][y] = 1
    number = arr[x][y]
    while q:
        x, y = q.popleft()
        ans.append((x, y))
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nx, ny = x+dx, (y+dy+m) % m
            if not (0 <= nx < n and 0 <= ny < m):
                continue
            if visited[nx][ny]:
                continue
            if arr[nx][ny] != number:
                continue
            visited[nx][ny] = 1
            q.append((nx, ny))
    if len(ans) == 1:
        return 0
    for x, y in ans:
        arr[x][y] = INF
    return len(ans)
        

def bomb():
    ret = 0
    visited = [[0]*m for __ in range(n)]
    for i in range(n):
        for j in range(m):
            if arr[i][j] == INF:
                continue
            if visited[i][j]:
                continue
            ret += bfs(visited, i, j)
    return ret

def arrange():
    s = 0
    c = 0
    for i in range(n):
        for j in range(m):
            if arr[i][j] == INF:
                continue
            s += arr[i][j]
            c += 1
    if c == 0:
        return
    avg = s / c
    for i in range(n):
        for j in range(m):
            if arr[i][j] == INF:
                continue
            if arr[i][j] > avg:
                arr[i][j] -= 1
            elif arr[i][j] < avg:
                arr[i][j] += 1

def get_sum():
    ret = 0
    for i in range(n):
        for j in range(m):
            if arr[i][j] == INF:
                continue
            ret += arr[i][j]
    return ret

def solve(x, d, k):
    if d == 0:
        move_clock_wise(x, k)
    else:
        move_counter_clock_wise(x, k)

    is_bombed = bomb()
    if not is_bombed:
        arrange()

for __ in range(t):
    x, d, k = map(int, input().split())
    solve(x, d, k)

print(get_sum())
