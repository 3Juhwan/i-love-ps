a = [1]
for i in range(2, 1000):
	p = a[-1] + i
	if p > 1000: break
	a.append(p)

v = [0]*10010
for i in a:
	for j in a:
		for k in a:
			v[i+j+k] = 1

for __ in range(int(input())):
	print(v[int(input())])
