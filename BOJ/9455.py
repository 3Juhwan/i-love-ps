for __ in range(int(input())):
	n, m = map(int, input().split())
	a = [list(map(int, input().split())) for __ in range(n)]
	ans = 0
	for i in range(m):
		cnt, ret = [0] * 2
		for j in range(n):
			cnt += a[j][i]
			ret += a[j][i] * (n - 1 - j)
		ans += ret - cnt * (cnt-1) // 2
	print(ans)
