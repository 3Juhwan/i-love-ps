arr = [list(map(int, input().split())) for __ in range(4)]
x, y = 0, 0
for k in range(1, 22):
    a, b = [-9] * 2
    for i in range(4):
        for j in range(5):
            if arr[i][j] == k:
                a, b = i, j
    if k == 1 or (abs(x-a) + abs(y-b) == 3 and x != a and y != b):
        x, y = a, b
        continue
    print(k-1)
    break
