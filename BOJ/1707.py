from collections import deque
import sys
input = lambda : sys.stdin.readline().rstrip()

MAX = 20_001

def solve():
    graph = [[] for __ in range(MAX)]
    v, e = map(int, input().split())
    for __ in range(e):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    
    visited = [-1]*MAX
    for k in range(1, v+1):
        if visited[k] != -1:
            continue
        visited[k] = 1
        q = deque([k])
        while q:
            x = q.popleft()
            for i in graph[x]:
                if visited[i] == -1:
                    visited[i] = reverse(visited[x])
                    q.append(i)
                elif visited[i] == visited[x]:
                    return 'NO'
    return 'YES'     

def reverse(x):
    if x == 1:
        return 2
    return 1

for __ in range(int(input())):
    print(solve())
