a1, b1, c1 = map(int, input().split())
a2, b2, c2 = map(int, input().split())
s1 = a1*3 + b1*20 + c1*120
s2 = a2*3 + b2*20 + c2*120
if s1 > s2:
    print("Max")
elif s1 < s2:
    print("Mel")
else:
    print("Draw")
