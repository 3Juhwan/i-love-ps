def ff(x):
        if x == '-': return 0
        if x == '\\': return 1
        if x == '(': return 2
        if x == '@': return 3
        if x == '?': return 4
        if x == '>': return 5
        if x == '&': return 6
        if x == '%': return 7
        if x == '/': return -1


while True:
        a = input()
        if a == '#':
                break
        ret = 0
        d = 1
        while a:
                ret += d * ff(a[-1])
                d *= 8
                a = a[:-1]
        print(ret)
