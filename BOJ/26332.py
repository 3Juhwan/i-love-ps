for __ in range(int(input())):
    a, b = map(int, input().split())
    print(a, b)
    print(b if a == 1 else a * b - 2 * (a - 1))
