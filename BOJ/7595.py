def star(x):
    for i in range(x):
        print('*'*(i+1))

n = int(input())
while n:
    star(n)
    n = int(input())
