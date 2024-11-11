import sys
input = lambda : sys.stdin.readline().rstrip()
INF = int(1e9)

ans = 0
block_id = 1
green = [[0]*4 for __ in range(6)]
blue = [[0]*4 for __ in range(6)]

def get_block_id():
    global block_id
    block_id += 1
    return block_id

def get_raw_blocks(t, x, y):
    blocks = []
    if t == 1:
        blocks.append((x, y))
    elif t == 2:
        blocks.append((x, y))
        blocks.append((x, y+1))
    elif t == 3:
        blocks.append((x, y))
        blocks.append((x+1, y))
    return blocks

def set_green_block(arr, t, x, y):
    blocks = get_raw_blocks(t, x, y)
    blocks.sort()
    margin = blocks[0][0]
    for i in range(len(blocks)):
        blocks[i] = (blocks[i][0]-margin, blocks[i][1])
    block_id = get_block_id()
    for x, y in blocks:
        arr[x][y] = block_id
    return blocks

def rotate_blocks(blocks):
    return [(y, x) for x, y in blocks]

def set_blue_block(arr, t, x, y):
    raw_blocks = get_raw_blocks(t, x, y)
    blocks = rotate_blocks(raw_blocks)
    margin = blocks[0][0]
    for i in range(len(blocks)):
        blocks[i] = (blocks[i][0]-margin, blocks[i][1])
    block_id = get_block_id()
    for x, y in blocks:
        arr[x][y] = block_id
    return blocks

def move_block(arr, blocks):
    blocks.sort(key=lambda x:-x[0])
    bottom_x = blocks[0][0]
    bottoms = [(x, y) for x, y in blocks if x == bottom_x]
    px = bottom_x+1
    while px < 6:
        is_blocked = 0
        for x, y in bottoms:
            if arr[px][y]:
                is_blocked = 1
        if is_blocked:
            break
        px += 1
    for x, y in blocks:
        block_id = arr[x][y]
        arr[x][y] = 0
        arr[x+(px-bottom_x-1)][y] = block_id
    return

def get_block(arr, x, y):
    block_id = arr[x][y]
    ret = [(x, y)]
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nx, ny = x+dx, y+dy
        if not (0 <= nx < 6 and 0 <= ny < 4):
            continue
        if arr[nx][ny] == block_id:
            ret.append((nx, ny))
    return ret

def bomb_block(arr):
    ret = 0
    for i in range(6):
        cnt = 0
        for j in range(4):
            if arr[i][j]:
                cnt += 1
        if cnt == 4:
            arr[i] = [0]*4
            ret += 1
    
    picked_block_id = set()
    for x in range(5, -1, -1):
        for y in range(4):
            block_id = arr[x][y]
            if block_id == 0:
                continue
            if block_id in picked_block_id:
                continue
            blocks = get_block(arr, x, y)
            move_block(arr, blocks)
            picked_block_id.add(block_id)
    return ret

def arrange_block(arr):
    while sum(arr[1]):
        del arr[-1]
        arr.insert(0, [0]*4)

def move_green(t, x, y):
    global ans
    blocks = set_green_block(green, t, x, y)
    move_block(green, blocks)
    bombed_cnt = INF
    while bombed_cnt > 0:
        bombed_cnt = bomb_block(green)
        ans += bombed_cnt
    arrange_block(green)

def move_blue(t, x, y):
    global ans
    blocks = set_blue_block(blue, t, x, y)
    move_block(blue, blocks)
    bombed_cnt = INF
    while bombed_cnt > 0:
        bombed_cnt = bomb_block(blue)
        ans += bombed_cnt
    arrange_block(blue)

for __ in range(int(input())):
    t, x, y = map(int, input().split())
    move_green(t, x, y)
    move_blue(t, x, y)

print(ans)
print(sum([1 if blue[i][j] else 0 for i in range(6) for j in range(4)]) + \
    sum([1 if green[i][j] else 0 for i in range(6) for j in range(4)]))
