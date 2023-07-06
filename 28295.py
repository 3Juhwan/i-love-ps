import sys
input = lambda : sys.stdin.readline().rstrip()

q = ['N', 'E', 'S', 'W']
psum = 400
for x in [int(input()) for __ in range(10)]:
    if x == 1:
        psum += 1
    elif x == 2:
        psum += 2
    elif x == 3:
        psum -= 1

print(q[psum%4])

