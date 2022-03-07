#9610 사분면
n = int(input())
x, y = [], []
axis, q1, q2, q3, q4 = 0, 0, 0, 0, 0

for i in range(n):
    xx, yy = map(int, input().split())
    x.append(xx)
    y.append(yy)
    if x[i] == 0 or y[i] == 0:
        axis += 1
    else:
        if x[i] > 0 and y[i] > 0:
            q1 += 1
        elif x[i] < 0 and y[i] > 0:
            q2 += 1
        elif x[i] < 0 and y[i] < 0:
            q3 += 1
        elif x[i] > 0 and y[i] < 0:
            q4 += 1
print("Q1:", q1)
print("Q2:", q2)
print("Q3:", q3)
print("Q4:", q4)
print("AXIS:", axis)