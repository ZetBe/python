#10214 Baseball
t = int(input())
for i in range(t):
    ys, kr = 0, 0
    for j in range(9):
        y, k = map(int, input().split())
        ys += y
        kr += k
    if ys > kr:
        print("Yonsei")
    if ys < kr:
        print("Korea")
    if ys == kr:
        print("Draw")