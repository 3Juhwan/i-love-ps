n = int(input())
while n%2 == 0:
    n //= 2
if n!=1: n = 0
print(n)
