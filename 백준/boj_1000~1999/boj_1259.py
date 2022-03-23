#1259 팰린드롬수
while True:
    n = int(input())
    a = []
    pal = 0
    if n == 0:
        break
    while n != 0:
        a.append(n%10)
        n //= 10
    for i in range(len(a)):
        if a[i] != a[len(a)-i-1]:
            pal = 1
    if pal == 1:
        print("no")
    else:
        print("yes")