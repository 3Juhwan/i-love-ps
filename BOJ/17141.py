from itertools import combinations as comb
from collections import deque
from copy import deepcopy as dc
import sys
input = lambda : sys.stdin.readline().rstrip()

n, m = map(int, input().split())
aaa = [list(map(int, input().split())) for __ in range(n)]
pos = []
for i in range(n):
    for j in range(n):
        if aaa[i][j] == 2:
            pos.append((i, j))

def solve(viruses):
    def isEnded():
        for i in range(n):
            for j in range(n):
                if arr[i][j] == 0:
                    return False
        return True

    def calculate():
        ans = 0
        for i in range(n):
            for j in range(n):
                ans = max(ans, arr[i][j])
        return ans

    arr = dc(aaa)
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 1:
                arr[i][j] = -1
            else: 
                arr[i][j] = 0
    
    for x, y in viruses:
        arr[x][y] = 1
    q = deque(viruses)
    while q:
        x, y = q.popleft()
        
        for dx, dy in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
            nx, ny = x+dx, y+dy
            if not (0 <= nx < n and 0 <= ny < n):
                continue
            if arr[nx][ny] == -1:
                continue
            if arr[nx][ny] > 0:
                continue
            q.append((nx, ny))
            arr[nx][ny] = arr[x][y]+1

    if isEnded():
        return calculate() - 1
    return 1000000000000000000

ans = 1000000000000000000
for viruses in comb(pos, m):
    ans = min(ans, solve(viruses))
print(ans if ans != 1000000000000000000 else -1)
