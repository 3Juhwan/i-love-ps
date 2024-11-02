from collections import deque
import sys
input = lambda : sys.stdin.readline().rstrip()
INF = int(1e9)

def find_a_and_b(arr):
    n, m = len(arr), len(arr[0])
    ret = []
    for i in range(n):
        for j in range(m):
            if arr[i][j] == '$':
                ret.append((i, j))
    return (ret[0], ret[1])

def get_min_dist_from(arr, x, y):
    n, m = len(arr), len(arr[0])
    visited = [[INF]*m for __ in range(n)]
    q = deque([(x, y)])
    visited[x][y] = 0
    while q:
        x, y = q.popleft()
        for dx, dy in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
            nx, ny = x+dx, y+dy
            if not (0 <= nx < n and 0 <= ny < m):
                continue
            if visited[nx][ny] != INF:
                continue
            if arr[nx][ny] == '*':
                continue
            if arr[nx][ny] == '#':
                q.append((nx, ny))
                visited[nx][ny] = visited[x][y] + 1
            else:
                q.appendleft((nx, ny))
                visited[nx][ny] = visited[x][y]
    return visited

def get_min_dist_from_point_to_exit(arr):
    n, m = len(arr), len(arr[0])
    visited = [[INF]*m for __ in range(n)]
    q = deque([])
    for i in range(n):
        for j in range(m):
            if i == 0 or i == n-1 or j == 0 or j == m-1:
                if arr[i][j] == '*':
                    continue
                if arr[i][j] == '#':
                    q.append((i, j))
                    visited[i][j] = 1
                else:
                    q.appendleft((i, j))
                    visited[i][j] = 0
    
    while q:
        x, y = q.popleft()
        for dx, dy in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
            nx, ny = x+dx, y+dy
            if not (0 <= nx < n and 0 <= ny < m):
                continue
            if visited[nx][ny] != INF:
                continue
            if arr[nx][ny] == '*':
                continue
            if arr[nx][ny] == '#':
                q.append((nx, ny))
                visited[nx][ny] = visited[x][y] + 1
            else:
                q.appendleft((nx, ny))
                visited[nx][ny] = visited[x][y]
    return visited

def get_common_way(arr):
    n, m = len(arr), len(arr[0])
    a, b = find_a_and_b(arr)
    ax, ay = a
    bx, by = b

    min_dist_from_a = get_min_dist_from(arr, ax, ay)
    min_dist_from_b = get_min_dist_from(arr, bx, by)
    min_dist_from_point_to_exit = get_min_dist_from_point_to_exit(arr)

    ans = INF
    for i in range(n):
        for j in range(m):
            if arr[i][j] == '#':
                ret = min_dist_from_point_to_exit[i][j] + min_dist_from_a[i][j] + min_dist_from_b[i][j]
                ans = min(ans, ret-2)
    return ans

def get_min_dist_to_exit(arr, x, y):
    rx, ry = x, y
    n, m = len(arr), len(arr[0])
    visited = [[INF]*m for __ in range(n)]
    q = deque([])
    for i in range(n):
        for j in range(m):
            if i == 0 or i == n-1 or j == 0 or j == m-1:
                if arr[i][j] == '*':
                    continue
                if arr[i][j] == '#':
                    q.append((i, j))
                    visited[i][j] = 1
                else:
                    q.appendleft((i, j))
                    visited[i][j] = 0
    
    while q:
        x, y = q.popleft()
        for dx, dy in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
            nx, ny = x+dx, y+dy
            if not (0 <= nx < n and 0 <= ny < m):
                continue
            if visited[nx][ny] != INF:
                continue
            if arr[nx][ny] == '*':
                continue
            if arr[nx][ny] == '#':
                q.append((nx, ny))
                visited[nx][ny] = visited[x][y] + 1
            else:
                q.appendleft((nx, ny))
                visited[nx][ny] = visited[x][y]
    return visited[rx][ry]

def get_each_way(arr):
    a, b = find_a_and_b(arr)
    ax, ay = a
    bx, by = b
    return get_min_dist_to_exit(arr, ax, ay) + get_min_dist_to_exit(arr, bx, by)

def solve():
    n, m = map(int, input().split())
    arr = [list(input()) for __ in range(n)]
    print(min(get_common_way(arr), get_each_way(arr)))

for __ in range(int(input())):
    solve()
