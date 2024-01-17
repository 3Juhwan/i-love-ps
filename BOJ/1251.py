a = input()
b = []
n = len(a)
for i in range(1, n-1):
	for j in range(i+1, n):
		b.append(a[:i][::-1] + a[i:j][::-1] + a[j:][::-1])
b.sort()
print(b[0])
