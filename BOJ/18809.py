import sys
input = lambda : sys.stdin.readline().rstrip()

n, m, g, r = map(int, input().split())
arr = [list(map(int, input().split())) for __ in range(n)]
all = [(x, y) for x in range(n) for y in range(m) if arr[x][y] == 2]

def solve(curG, curR):
    ans = 0
    visited = setUp()
    for x, y in curG: visited[x][y] = 0
    for x, y in curR: visited[x][y] = 0
    nextG, nextR = [], []
    while curG and curR:
        for x, y in curG:
            # 꽃이 피어난 곳, 아름다울지도
            if visited[x][y] == -1:
                continue
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx, ny = x+dx, y+dy
                if nx < 0 or nx >= n or ny < 0 or ny >= m:
                    continue
                if visited[nx][ny] == 0 or visited[nx][ny] == 1 or visited[nx][ny] == -1:
                    continue
                visited[nx][ny] = 1
                nextG.append((nx, ny))

        for x, y in curR:
            # 꽃이 피어난 곳, 아름다울지도
            if visited[x][y] == -1:
                continue
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx, ny = x+dx, y+dy
                if nx < 0 or nx >= n or ny < 0 or ny >= m:
                    continue
                if visited[nx][ny] == 0 or visited[nx][ny] == 2 or visited[nx][ny] == -1:
                    continue
                if visited[nx][ny] == 1:
                    visited[nx][ny] = -1
                    ans += 1
                    continue
                visited[nx][ny] = 2
                nextR.append((nx, ny))
        for x, y in nextG:
            if visited[x][y] == 1 or visited[x][y] == 2:
                visited[x][y] = 0
        for x, y in nextR:
            if visited[x][y] == 1 or visited[x][y] == 2:
                visited[x][y] = 0
        curG, curR = nextG, nextR
        nextG, nextR = [], []
    return ans

def setUp():
    visited = [[9]*m for __ in range(n)]
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 0:
                visited[i][j] = 0
    return visited

comb = []
greenBag = []
redBag = []
ans = 0

def combination(cnt, g, r):
    global ans
    if not g and not r:
        ans = max(ans, solve(greenBag, redBag))
        return
    if len(all)-cnt < g+r:
        return
    if g:
        for i in range(cnt, len(all)):
            if len(all)-i < g+r:
                break
            greenBag.append(all[i])
            combination(i+1, g-1, r)
            greenBag.pop()
    if r:
        for i in range(cnt, len(all)):
            if len(all)-i < g+r:
                break
            redBag.append(all[i])
            combination(i+1, g, r-1)
            redBag.pop()

combination(0, g, r)
print(ans)
