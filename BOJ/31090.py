for __ in range(int(input())):
    n = int(input())
    print("Bye" if (n+1) % (n%100) else "Good")
