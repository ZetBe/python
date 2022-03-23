#네 번째 점 백준
#3009
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))
d = []
if a[0] == b[0]:
    d.append(c[0])
if b[0] == c[0]:
    d.append(a[0])
if c[0] == a[0]:
    d.append(b[0])

if a[1] == b[1]:
    d.append(c[1])
if b[1] == c[1]:
    d.append(a[1])
if c[1] == a[1]:
    d.append(b[1])

print("%d %d"%(d[0], d[1]))