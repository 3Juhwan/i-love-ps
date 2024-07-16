import sys
input = lambda : sys.stdin.readline().rstrip()

n = int(input())
arr = list(map(int, input().split()))
arr.sort()

ans = (4_000_000_002, [])
for i in range(n):
    for j in range(i+1, n):
        a, b = arr[i], arr[j]
        diff = -(a+b)

        start, end = j, n
        while start + 1 < end:
            mid = (start + end) // 2
            if arr[mid] >= diff:
                end = mid
            else:
                start = mid
        
        target = []
        if end != j+1:
            target.append(end-1)
        if end != n:
            target.append(end)

        for x in target:
            tmp = a + b + arr[x]
            if abs(tmp) < ans[0]:
                ans = (abs(tmp), [a, b, arr[x]])

print(*ans[1])
