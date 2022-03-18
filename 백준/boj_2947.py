#2947 나무 조각
a = list(map(int, input().split()))
while True:
    if a[0] > a[1]:
        a[0], a[1] = a[1], a[0]
        print(a[0], a[1], a[2], a[3], a[4])
    if a[1] > a[2]:
        a[1], a[2] = a[2], a[1]
        print(a[0], a[1], a[2], a[3], a[4])
    if a[2] > a[3]:
        a[2], a[3] = a[3], a[2]
        print(a[0], a[1], a[2], a[3], a[4])
    if a[3] > a[4]:
        a[3], a[4] = a[4], a[3]
        print(a[0], a[1], a[2], a[3], a[4])
    if a[0] == 1 and a[1] == 2 and a[2] == 3 and a[3] == 4 and a[4] == 5:
        break