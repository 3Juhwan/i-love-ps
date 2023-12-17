for __ in range(int(input())):
    a1, b1, a2, b2 = map(int, input().split())
    if a1*b1 > a2*b2:
        print("TelecomParisTech")
    elif a1*b1 < a2*b2:
        print("Eurecom")
    else:
        print("Tie")
