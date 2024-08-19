from collections import deque
import sys
input = lambda : sys.stdin.readline().rstrip()

n, m = map(int, input().split())
visited = [0]*101

bridge, bam = {}, {}
for __ in range(n):
    a, b = map(int, input().split())
    bridge[a] = b
for __ in range(m):
    a, b = map(int, input().split())
    bam[a] = b

cur = 1
q = deque([1])
while q:
    x = q.popleft()
    for i in range(1, 7):
        nx = x+i
        if nx in bridge:
            visited[nx] = visited[x] + 1
            nx = bridge[nx]
        if nx in bam:
            visited[nx] = visited[x] + 1
            nx = bam[nx]
        if nx > 100:
            continue
        if visited[nx]:
            continue
        q.append(nx)
        visited[nx] = visited[x] + 1

print(visited[100])
