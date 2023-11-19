n = int(input())
arr = [int(input()[2:]) for __ in range(n)]
print(len([x for x in arr if x <= 90]))
