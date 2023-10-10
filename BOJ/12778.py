digit = "0ABCDEFGHIJKLMNOPQRSTUVWXYZ"

for __ in range(int(input())):
    a, b = input().split()
    for x in input().split():
        if b == "C":
            print(digit.index(x), end=' ')
        else:
            print(digit[int(x)], end=' ')
    print()
