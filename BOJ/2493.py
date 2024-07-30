import sys
input = lambda : sys.stdin.readline().rstrip()

n = int(input())
arr = list(map(int, input().split()))

stack = []

ans = []

for i in range(n):
    x = arr[i]
    while stack and arr[stack[-1]] < x:
        stack.pop()
    
    if not stack:
        ans.append(0)
        stack.append(i)
        continue

    ans.append(stack[-1] + 1)
    stack.append(i)

print(*ans)
