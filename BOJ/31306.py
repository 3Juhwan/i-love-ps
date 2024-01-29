a, b = 0, 0
for x in input():
    if x in 'aeiou':
        a += 1
    if x in 'y':
        b += 1
print(a, a + b)
