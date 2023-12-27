input()
a = list(map(int, input().split()))
b = 8 * (len(a) - 1) + sum(a)
print(b // 24, b % 24)
