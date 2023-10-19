a = list(map(int, input().split()))
a.sort()
print(max(abs(a[1]-a[0]-1),abs(a[2]-a[1]-1)))
