for __ in range(int(input())):
	a, b, c = map(float, input().split())
	print("${:.2f}".format(round(a*b*c, 2)))
