#11758 CCW
p1 = list(map(int, input().split()))
p2 = list(map(int, input().split()))
p3 = list(map(int, input().split()))
s = ((p2[0] - p1[0]) * (p3[1] - p1[1])) - ((p2[1] - p1[1]) * (p3[0] - p1[0]))
if s > 0:
    print(1)
elif s == 0:
    print(0)
else:
    print(-1)