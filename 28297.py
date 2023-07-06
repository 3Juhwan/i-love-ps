from math import sqrt, pi, acos
import sys
input = lambda : sys.stdin.readline().rstrip()


def duplicate(gears, i, j):
    x1, y1, r1 = gears[i]
    x2, y2, r2 = gears[j]
    return r1+r2 >= sqrt((x1-x2)**2+(y1-y2)**2)


def dist(gears, i, j):
    if gears[i][2] < gears[j][2]:
        i, j = j, i

    x1, y1, r1 = gears[i]
    x2, y2, r2 = gears[j]

    xdiff_square = (x1-x2)**2
    ydiff_square = (y1-y2)**2
    rdiff = r1-r2

    if r1 == r2:
        return 2*pi*r1 + 2*sqrt(xdiff_square + ydiff_square)
    
    return  2 * sqrt(xdiff_square + ydiff_square - (rdiff)**2)\
            + 2 * r1 * pi\
            - 2 * (rdiff) * acos((rdiff) / sqrt(xdiff_square + ydiff_square))


def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]


def union(parent, x, y):
    a, b = find(parent, x), find(parent, y)
    if a>b:
        parent[a] = b
    else:
        parent[b] = a


def same(x, y):
    a, b = find(x), find(y)
    return a==b


n = int(input())
gears = [list(map(int, input().split())) for __ in range(n)]

info = []
for i in range(n):
    for j in range(i+1, n):
        if duplicate(gears, i, j):
            info.append((0, i, j))
            continue
        info.append((dist(gears, i, j), i, j))

info.sort()

parent = list(range(n))


psum = 0
for d, i, j in info:
    if duplicate(gears, i, j):
        union(parent, i, j)
        continue

    if find(parent, i) == find(parent, j):
        continue

    psum += dist(gears, i, j)
    union(parent, i, j)

print(psum)
