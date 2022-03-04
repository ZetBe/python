#5355 화성 수학
t = int(input())
a = []
for i in range(t):
    a = list(input().split())
    a[0] = float(a[0])
    for j in range(1, len(a)):
        if a[j] == '@':
            a[0] *= 3
        elif a[j] == '%':
            a[0] += 5
        elif a[j] == '#':
            a[0] -= 7
    print("{:.2f}".format(a[0]))