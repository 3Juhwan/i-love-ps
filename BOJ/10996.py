n = int(input())
if n == 1:
	print("*")
else:
	for i in range(2*n):
		for j in range(n):
			if i%2 == j%2:
				print("*", end="")
			else:
				print(" ", end="")
		print()
