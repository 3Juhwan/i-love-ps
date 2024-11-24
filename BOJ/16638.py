import sys
sys.setrecursionlimit(2**22)
input = lambda : sys.stdin.readline().rstrip()
INF = int(1e9)

n = int(input())
arr = input()
numbers = list(map(int, arr[::2]))
operators = list(arr[1::2])
prior = [1]*len(operators)
for i in range(len(operators)):
    if operators[i] == '*':
        prior[i] = 2

ans = -INF

def cal(a, operator, b):
    if operator == '+':
        return a+b
    elif operator == '-':
        return a-b
    elif operator == '*':
        return a*b

def calculate():
    nums = numbers[::]
    opers = operators[::]
    pr = prior[::]
    nums_buf = [nums[0]]
    for i in range(len(pr)):
        if pr[i] == 3:
            nums_buf.append(cal(nums_buf.pop(), opers[i], nums[i+1]))
        else:
            nums_buf.append(nums[i+1])

    nums = nums_buf
    nums_buf = [nums[0]]
    for i in range(len(pr)):
        if pr[i] == 3:
            pr[i] = -1
            opers[i] = ''
    opers = [x for x in opers if x != '']
    pr = [x for x in pr if x != -1]

    for i in range(len(pr)):
        if pr[i] == 2:
            nums_buf.append(cal(nums_buf.pop(), opers[i], nums[i+1]))
        else:
            nums_buf.append(nums[i+1])
    
    nums = nums_buf
    nums_buf = [nums[0]]
    for i in range(len(pr)):
        if pr[i] == 2:
            pr[i] = -1
            opers[i] = ''
    opers = [x for x in opers if x != '']
    pr = [x for x in pr if x != -1]

    for i in range(len(pr)):
        if pr[i] == 1:
            nums_buf.append(cal(nums_buf.pop(), opers[i], nums[i+1]))
        else:
            nums_buf.append(nums[i+1])

    return nums_buf[0]

def dfs(idx):
    global ans
    if idx >= len(prior):
        ans = max(ans, calculate())
        return 

    if idx == 0 or prior[idx-1] != 3:
        tmp = prior[idx]
        prior[idx] = 3
        dfs(idx+2)
        prior[idx] = tmp
    dfs(idx+1)
        
dfs(0)
print(ans)
