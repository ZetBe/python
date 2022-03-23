#2476 주사위 게임
n = int(input())
price = []
for i in range(n):
    a, b, c = map(int, input().split())
    if a == b and b == c:
        price.append(10000 + 1000*a)
    if a == b and b != c:
        price.append(1000 + 100*a)
    if a == c and a != b:
        price.append(1000 + 100*a)
    if b == c and a != b:
        price.append(1000 + 100*b)
    if a != b and b != c and c != a:
        ma = a
        if ma < b:
            ma = b
        if ma < c:
            ma = c
        price.append(100 * ma)
price.sort()
print(price[n-1])