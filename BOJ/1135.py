import sys
input = lambda : sys.stdin.readline().rstrip()

n = int(input())
tree = [[] for __ in range(n)]
tmp = list(map(int, input().split()))
for i in range(1, n):
    x = tmp[i]
    tree[x].append(i)

def dfs(cur):
    if not tree[cur]:
        return 0

    tmp = []
    for x in tree[cur]:
        tmp.append(dfs(x))
    tmp.sort()
    
    ret = 0
    for i in range(len(tmp)):
        ret = max(ret, len(tmp) - i + tmp[i])
    return ret
        
print(dfs(0))
