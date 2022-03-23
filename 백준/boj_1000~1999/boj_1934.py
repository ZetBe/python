#1934 최소공배수
t = int(input())
for i in range(t):
    a, b = map(int, input().split())
    aa, bb = a, b
    while aa != 0 and bb != 0:
        if aa > bb:
            aa %= bb
        else:
            bb %= aa
    if aa != 0:
        c = aa
    else:
        c = bb
    d = a*b//c
    print(d)