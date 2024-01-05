a = {'a': '4', 'e': '3', 'i': '1', 'o': '0', 's': '5'}
print(''.join(a[x] if x in a else x for x in input()))
