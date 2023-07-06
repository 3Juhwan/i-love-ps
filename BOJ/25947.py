import sys
input = lambda : sys.stdin.readline().rstrip()

n, b, a = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

idx = 0
psum = 0
ans = -1
for i in range(n):
    psum += arr[i] // 2
    while (psum > b or i-idx >= a) and idx <= i:
        psum += arr[idx] // 2
        idx += 1
    print(idx, i)
    if psum > b:
        break

    ans = i

print(ans+1)