#터렛 백준
#1002
import math
T = int(input())
for i in range(T):
    x_dist = float()
    y_dist = float()
    dist = float()
    x_1, y_1, r_1, x_2, y_2, r_2 = map(int, input().split())
    if x_1 > x_2:
        x_dist = (x_1 - x_2)**2
    else:
        x_dist = (x_2 - x_1)**2

    if y_1 > y_2:
        y_dist = (y_1 - y_2)**2
    else:
        y_dist = (y_2 - y_1)**2

    dist = y_dist + x_dist
    dist = math.sqrt(dist)
    if r_1 > r_2:
        a = r_1 - r_2
    else:
        a = r_2 - r_1

    if dist == 0 and a == 0:
        print(-1)
    elif dist < r_1 + r_2 and (dist > a):
        print(2)
    elif dist == r_1 + r_2 or dist == a:
        print(1)
    else:
        print(0)
