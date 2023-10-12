while True:
        a = input()
        if a == "#": break
        a = a.lower()
        a = set(list(a))
        ans = 0
        for x in "qwertyuiopasdfghjklzxcvbnm":
                ans += (1 if x in a else 0)
        print(ans)
