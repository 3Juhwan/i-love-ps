from collections import deque
import sys
input = lambda : sys.stdin.readline().rstrip()
INF = int(1e9)

def get_result(n, m):
    arr = [list(input()) for __ in range(n)]
    node = []
    for i in range(n):
        for j in range(m):
            if arr[i][j] in 'o*':
                node.append((i, j))
    
    node_cnt = len(node) # max: 400
    dist = [[INF]*node_cnt for __ in range(node_cnt)] # max: 160_000

    for i in range(node_cnt):
        x, y = node[i]
        visited = [[0]*m for __ in range(n)]
        q = deque([(x, y, 0)])
        visited[x][y] = 1
        while q:
            a, b, d = q.popleft()
            if arr[a][b] in 'o*':
                dist[i][node.index((a, b))] = min(dist[i][node.index((a, b))], d)
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx, ny = a+dx, b+dy
                if not (0 <= nx < n and 0 <= ny < m):
                    continue
                if visited[nx][ny]:
                    continue
                if arr[nx][ny] == 'x':
                    continue
                q.append((nx, ny, d+1))
                visited[nx][ny] = 1
    
    robot = -1
    for i in range(node_cnt):
        x, y = node[i]
        if arr[x][y] == 'o':
            robot = i

    for i in range(node_cnt):
        for j in range(node_cnt):
            if dist[i][j] == INF:
                return -1
    
    visited = [0]*node_cnt
    ans = INF
    def dfs(x, w):
        nonlocal ans

        if sum(visited) == node_cnt:
            ans = min(ans, w)
            return
        for i in range(node_cnt):
            if visited[i]:
                continue
            visited[i] = 1
            dfs(i, w + dist[x][i])
            visited[i] = 0
    
    visited[robot] = 1
    dfs(robot, 0)
    return ans
    
def solve():
    while True:
        m, n = map(int, input().split())
        if n == 0 and m == 0:
            return
        print(get_result(n, m))

solve()
