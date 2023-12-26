arr = [int(input()) for __ in range(5)]
for x in arr:
    if arr.count(x) % 2:
        print(x)
        break
