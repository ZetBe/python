#9506 약수들의 합
while True:
    n = int(input())
    a = []
    aa = 0
    if n == -1:
        break
    nn = n
    for i in range(1, nn):
        if n % i == 0:
            a.append(i)
            aa += i
    if aa == n:
        print("%d = "%(n), end='')
        for j in range(len(a)-1):
            print("%d + "%(a[j]), end='')
        print(a[len(a)-1])
    else:
        print("%d is NOT perfect."%(n))