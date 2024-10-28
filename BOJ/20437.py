from collections import deque
import sys
input = lambda : sys.stdin.readline().rstrip()

def solve(arr, k):
    ans_min, ans_max = 1010101, -1
    dic = {}
    for i in range(len(arr)):
        x = arr[i]
        if x in dic:
            dic[x].append(i)
        else:
            dic[x] = deque([i])
        if len(dic[x]) == k:
            ans_min = min(ans_min, 1 + dic[x][-1] - dic[x][0])
            ans_max = max(ans_max, 1 + dic[x][-1] - dic[x][0])
            dic[x].popleft()
    return (ans_min, ans_max)

for __ in range(int(input())):
    ans = solve(input(), int(input()))
    if ans[1] == -1:
        print(-1)
    else:
        print(*ans)
