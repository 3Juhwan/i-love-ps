while True:
    try:
        for x in input():
            if x == 'i':
                print('e', end='')
            elif x == 'e':
                print('i', end='')
            elif x == 'I':
                print('E', end='')
            elif x == 'E':
                print('I', end='')
            else:
                print(x, end='')
        print()
    except:
        break
