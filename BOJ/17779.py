import sys
input = lambda : sys.stdin.readline().rstrip()


def getNumberOfFirstSectionPeople(arr, n, x, y, d1, d2):
    ret = 0
    for i in range(n):
        for j in range(n):
            if i+j >= x+y : continue
            if i >= x+d1: continue
            if j > y: continue
            ret += arr[i][j]
    return ret


def getNumberOfSecondSectionPeople(arr, n, x, y, d1, d2):
    ret = 0
    for i in range(n):
        for j in range(n):
            if j-i <= y-x: continue
            if i > x+d2: continue
            if j <= y: continue
            ret += arr[i][j]
    return ret

    
def getNumberOfThirdSectionPeople(arr, n, x, y, d1, d2):
    ret = 0
    for i in range(n):
        for j in range(n):
            if j-i >= y-x-2*d1: continue
            if i < x+d1: continue
            if j >= y-d1+d2: continue
            ret += arr[i][j]
    return ret


def getNumberOfFourthSectionPeople(arr, n, x, y, d1, d2):
    ret = 0
    for i in range(n):
        for j in range(n):
            if i+j <= x+y+2*d2: continue
            if i <= x+d2: continue
            if j < y-d1+d2: continue
            ret += arr[i][j]
    return ret


def getNumberOfFifthSectionPeople(arr, n, x, y, d1, d2):
    ret = 0
    for i in range(n):
        for j in range(n):
            if i+j < x+y : continue
            if j-i > y-x: continue
            if j-i < y-x-2*d1: continue
            if i+j > x+y+2*d2: continue
            ret += arr[i][j]
    return ret


def solve():
    n = int(input())
    arr = [list(map(int, input().split())) for __ in range(n)]

    ans = int(1e20)

    for x in range(n):
        for y in range(n):
            for d1 in range(1, n):
                for d2 in range(1, n):
                    if x+d1+d2 >= n: break
                    if y+d2 >= n: break

                    section = []
                    section.append(getNumberOfFirstSectionPeople(arr, n, x, y, d1, d2))
                    section.append(getNumberOfSecondSectionPeople(arr, n, x, y, d1, d2))
                    section.append(getNumberOfThirdSectionPeople(arr, n, x, y, d1, d2))
                    section.append(getNumberOfFourthSectionPeople(arr, n, x, y, d1, d2))
                    section.append(getNumberOfFifthSectionPeople(arr, n, x, y, d1, d2))

                    ans = min(ans, max(section)-min(section))
    
    print(ans)

solve()