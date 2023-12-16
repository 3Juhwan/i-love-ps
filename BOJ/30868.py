for i in range(int(input())):
    n = int(input())
    a = "++++ " * (n//5)
    a += "|" * (n%5)
    print(a)
