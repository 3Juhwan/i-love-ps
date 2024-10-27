from bisect import bisect_left
import sys
input = lambda : sys.stdin.readline().rstrip()

start = {}
end = {}
for __ in range(int(input())):
    l, r = map(int, input().split())
    if l in start:
        start[l].append(r)
    else:
        start[l] = [r]
    if r in end:
        end[r].append(l)
    else:
        end[r] = [l]

for x in start:
    start[x].sort()
for x in end:
    end[x].sort()

def solve(l, r):
    if l in start and bisect_left(start[l], r) < len(start[l]) and start[l][bisect_left(start[l], r)] == r:
        return 1
    if l in start and bisect_left(start[l], r) < len(start[l]) and start[l][bisect_left(start[l], r)] > r \
        and r in end and 0 < bisect_left(end[r], l) and end[r][bisect_left(end[r], l) - 1] < l:
        return 2
    return -1

for __ in range(int(input())):
    l, r = map(int, input().split())
    print(solve(l, r))
