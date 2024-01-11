def f(x):
    if x>=300:return 1
    elif x>=275:return 2
    elif x>=250:return 3
    return 4
input(); 
for x in list(map(int, input().split())):
    print(f(x))

