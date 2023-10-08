n = int(input())
arr = list(map(int, input().split()))
ans = []
for i in range(n):
	if not ans:
		ans.append([arr[i]])
		continue
	if ans[-1][-1] < arr[i]:
		ans[-1].append(arr[i])
	else:
		ans.append([arr[i]])
ret = 0
for x in ans:
	ret = max(ret, x[-1]-x[0])
print(ret)
