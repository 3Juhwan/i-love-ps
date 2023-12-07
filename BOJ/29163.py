input()
a = list(map(int, input().split()))
cnt1, cnt2 = [0] * 2
for x in a:
    if x%2 == 0:
        cnt1 += 1
    else:
        cnt2 += 1
if cnt1 > cnt2:
    print("Happy")
else:
    print("Sad")
