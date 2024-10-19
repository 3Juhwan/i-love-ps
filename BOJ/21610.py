import sys
input = lambda : sys.stdin.readline().rstrip()

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for __ in range(n)]
dir = [(), (0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1)]
visited = [[0]*n for __ in range(n)]

def move_position(x, y, dx, dy):
    nx, ny = x + dx, y + dy
    nx, ny = (nx+100*n) % n, (ny+100*n) % n
    return (nx, ny)

def move(clouds, d, s):
    global visited
    dx, dy = dir[d]
    new_visited = [[0]*n for __ in range(n)]
    for i in range(len(clouds)):
        x, y = clouds[i]
        nx, ny = move_position(x, y, dx*s, dy*s)
        new_visited[nx][ny] = 1
        clouds[i] = (nx, ny)
    visited = new_visited

def rain_down(clouds):
    for x, y in clouds:
        arr[x][y] += 1

def water_duplicate(clouds):
    diagonal_dir = [(-1, -1), (1, 1), (-1, 1), (1, -1)]
    for x, y in clouds:
        for dx, dy in diagonal_dir:
            nx, ny = x+dx, y+dy
            if not (0 <= nx < n and 0 <= ny < n):
                continue
            arr[x][y] += 1 if arr[nx][ny] else 0

def generate_clouds(clouds):
    new_clouds = []
    for x in range(n):
        for y in range(n):
            if arr[x][y] >= 2 and not visited[x][y]:
                new_clouds.append((x, y))
                arr[x][y] -= 2
    
    for x, y in clouds:
        visited[x][y] = 0
    for x, y in new_clouds:
        visited[x][y] = 1
    return new_clouds

def solve(m):
    clouds = [(n-1, 0), (n-1, 1), (n-2, 0), (n-2, 1)]
    visited[n-1][0], visited[n-1][1], visited[n-2][0], visited[n-2][1] = [1]*4

    for __ in range(m):
        d, s = map(int, input().split())
        move(clouds, d, s)
        rain_down(clouds)
        water_duplicate(clouds)
        clouds = generate_clouds(clouds)

solve(m)
print(sum([arr[x][y] for x in range(n) for y in range(n)]))
