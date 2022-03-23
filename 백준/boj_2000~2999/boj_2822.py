#2822 점수 계산
b = [1, 2, 3, 4, 5, 6, 7, 8]
a = []
for i in range(8):
    a.append(int(input()))
for n in range(7):
    for m in range(n+1, 8):
        if a[n] >= a[m]:
            a[n], a[m], b[n], b[m] = a[m], a[n], b[m], b[n]
c = 0
d = []
for v in range(5):
    c += a[7-v]
    d.append(b[7-v])
print(c)
d.sort()
print(d[0], d[1], d[2], d[3], d[4])