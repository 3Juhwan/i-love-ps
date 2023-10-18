while True:
	a = input()
	if a[0] == '0': break
	b = '-'
	for x in a[2:].split():
		if x != b:
			print(x, end=' ')
		b = x	
	print('$')

