import sys
sys.setrecursionlimit(10_000_000)
input = lambda : sys.stdin.readline().rstrip()

n = int(input())
graph = [[] for __ in range(n+1)]
for __ in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

INF = int(1e9)
dp = [[INF]*2 for __ in range(n+1)]

def solve(node, prev, status):
    if len(graph[node]) == 1 and node != 1:
        dp[node][status] = 1 if status else 0
        return dp[node][status]

    if dp[node][status] != INF:
        return dp[node][status]
    
    ret = 0
    if status:
        ret += 1
        for x in graph[node]:
            if prev == x:
                continue
            ret += min(solve(x, node, status), solve(x, node, not status))
    else:
        for x in graph[node]:
            if prev == x:
                continue
            ret += solve(x, node, not status)
    dp[node][status] = ret
    return dp[node][status]

solve(1, 0, 0)
solve(1, 0, 1)

print(min(dp[1]))
