#13458 시험 감독
n = int(input())
a = list(map(int, input().split()))
peo = 0
b, c = map(int, input().split())
for i in range(n):
    a[i] -= b
    peo += 1
    if a[i] >= 0:
        if a[i]/c > a[i]//c:
            peo += (a[i]//c)+1
        else:
             peo += a[i]//c


print(peo)