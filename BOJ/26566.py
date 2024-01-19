for __ in range(int(input())):
    a, p1 = map(int, input().split())
    b, p2 = map(int, input().split())
    print(["Slice of pizza", "Whole pizza"][a/p1 < 3.14*b*b/p2])
