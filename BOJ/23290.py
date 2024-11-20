import sys
input = lambda : sys.stdin.readline().rstrip()
INF = int(1e9)

dir = [(0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1)]
shark_dir = [(-1, 0), (0, -1), (1, 0), (0, 1)]
shark_dir_comb = []

def dfs(arr):
    if len(arr) == 3:
        shark_dir_comb.append(arr[::])
        return
    for i in range(4):
        arr.append(shark_dir[i])
        dfs(arr)
        arr.pop()

dfs([])
m, s = map(int, input().split())
fish = [[x-1 for x in map(int, input().split())] for __ in range(m)]
shark = tuple([x-1 for x in map(int, input().split())])
smell = [[0]*4 for __ in range(4)]

def move_fish():
    global fish
    ret = []
    for x, y, d in fish:
        for i in range(8):
            dd = (d-i+8)%8
            dx, dy = dir[dd]
            nx, ny = x+dx, y+dy
            if not (0 <= nx < 4 and 0 <= ny < 4):
                continue
            if shark == (nx, ny):
                continue
            if smell[nx][ny]:
                continue
            ret.append((nx, ny, dd))
            break
        else:
            ret.append((x, y, d))
    fish = ret

def move_shark():
    global fish, smell, shark
    max_move = []
    max_cnt = -1
    for i in range(len(shark_dir_comb)):
        dirs = shark_dir_comb[i]
        cur = []
        x, y = shark
        for dx, dy in dirs:
            x, y = x+dx, y+dy
            if not (0 <= x < 4 and 0 <= y < 4):
                continue
            cur.append((x, y))
        if len(cur) != 3:
            continue
        cnt = 0
        for x, y, d in fish:
            if (x, y) in cur:
                cnt += 1
        if max_cnt < cnt:
            max_cnt = cnt
            max_move = cur
    shark = max_move[-1]
    ret = []
    for x, y, d in fish:
        if (x, y) not in max_move:
            ret.append((x, y, d))
        else:
            smell[x][y] = 2
    fish = ret
    return max_move

def delete_smell():
    for i in range(4):
        for j in range(4):
            if smell[i][j]:
                smell[i][j] -= 1

def append_fish(copy_fish):
    global fish
    for x, y, d in copy_fish:
        fish.append((x, y, d))

for __ in range(s):
    copy_fish = fish[::]
    move_fish()
    delete_smell()
    die_fish = move_shark()
    append_fish(copy_fish)

print(len(fish))
