from collections import deque
import sys
input = lambda : sys.stdin.readline().rstrip()

MAX = 201
a, b, c = map(int, input().split())
v = [[0]*MAX for __ in range(MAX)]
v[0][0] = 1
total = c
q = deque([(0, 0)])
while q:
    ta, tb = q.popleft()
    tc = total - ta - tb

    # a -> b
    if tb != b and ta:
        move = min(b-tb, ta)
        db = tb + move
        da = ta - move
        if not v[da][db]:
            q.append((da, db))
            v[da][db] = 1

    # a -> c
    if tc != c and ta:
        move = min(c-tc, ta)
        dc = tc + move
        da = ta - move
        if not v[da][total-da-dc]:
            q.append((da, total-da-dc))
            v[da][total-da-dc] = 1

    # b -> a
    if ta != a and tb:
        move = min(a-ta, tb)
        da = ta + move
        db = tb - move
        if not v[da][db]:
            q.append((da, db))
            v[da][db] = 1

    # b -> c
    if tc != c and tb:
        move = min(c-tc, tb)
        dc = tc + move
        db = tb - move
        if not v[total-db-dc][db]:
            q.append((total-db-dc, db))
            v[total-db-dc][db] = 1

    # c -> a
    if ta != a and tc:
        move = min(a-ta, tc)
        da = ta + move
        dc = tc - move
        if not v[da][total-da-dc]:
            q.append((da, total-da-dc))
            v[da][total-da-dc] = 1

    # c -> b
    if tb != b and tc:
        move = min(b-tb, tc)
        db = tb + move
        dc = tc - move
        if not v[total-db-dc][db]:
            q.append((total-db-dc, db))
            v[total-db-dc][db] = 1

ans = set()
for i in range(MAX):
    if v[0][i]:
        ans.add(total-i)
print(*sorted(list(ans)))
