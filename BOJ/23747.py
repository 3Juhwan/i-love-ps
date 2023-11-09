from collections import deque
import sys
input = lambda : sys.stdin.readline().rstrip()

n, m = map(int, input().split())
arr = [list(input()) for __ in range(n)]
x, y = map(int, input().split())
x, y = x-1, y-1

result = [list('#'*m) for __ in range(n)]

dir = {'L': (0, -1), 'R': (0, 1), 'U': (-1, 0), 'D': (1, 0)}

def ff(x, y):
        flag = arr[x][y]
        q = deque([(x, y)])
        while q:
                x, y = q.popleft()
                for way in 'LRUD':
                        nx, ny = x+dir[way][0], y+dir[way][1]
                        if nx < 0 or nx >= n or ny < 0 or ny >= m:
                                continue
                        if result[nx][ny] == '.':
                                continue
                        if arr[nx][ny] != flag:
                                continue
                        result[nx][ny] = '.'
                        q.append((nx, ny))



for way in input():
        if way == 'W':
                if result[x][y] == '.':
                        continue
                ff(x, y)
                continue
        nx, ny = dir[way]
        x, y = x+nx, y+ny

result[x][y] = '.'
for way in 'LRUD':
        nx, ny = x+dir[way][0], y+dir[way][1]
        if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
        result[nx][ny] = '.'

for i in result:
        for j in i:
                print(j, end='')
        print()
