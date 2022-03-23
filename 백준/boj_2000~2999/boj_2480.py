#2480 주사위 세개
a, b, c = map(int, input().split())
if a == b:
    if b == c:
        price = 10000 + 1000*a
    elif b != c:
        price = 1000 + 100*a
else:
    if (b == c and c != a) or (b != c and c == a):
        price = 1000 + 100*c
    if b != c and c != a:
        max = 0
        if max < a:
            max = a
        if max < b:
            max = b
        if max < c:
            max = c
        price = 100*max
print(price)