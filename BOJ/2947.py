a = list(map(int, input().split()))
for i in range(len(a)):
	for j in range(0, len(a)-1):
		if a[j] > a[j+1]:
			a[j], a[j+1] = a[j+1], a[j]
			print(*a)
	if a == list(sorted(a)):
		break
