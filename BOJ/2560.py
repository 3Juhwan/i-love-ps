from collections import deque
import sys
input = lambda : sys.stdin.readline().rstrip()

a, b, d, n = map(int, input().split())
q = deque([0]*d)
q[0] = 1
p = 0
for __ in range(n):
    q.pop()
    q.appendleft(0)
    p = p - q[b] + q[a]
    q[0] = p % 1000

print(sum(q) % 1000)
