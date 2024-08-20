import sys

input = lambda : sys.stdin.readline().rstrip()

n = int(input())
arr = list(map(int, input().split()))

lo, hi = 0, len(arr) - 1
ans = 999_999_999_999_999_999_999_999_999
while lo < hi:
    if abs(ans) > abs(arr[lo] + arr[hi]):
        ans = arr[lo] + arr[hi]
    if abs(arr[lo]) < abs(arr[hi]):
        hi -= 1
    else:
        lo += 1

print(ans)
