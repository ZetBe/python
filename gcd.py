def gcd_sub(a, b):
    while b > 0:
        a, b = a - b, b
        if a == b:
            break
        if b > a:
            a, b = b, a

    return a


def gcd_mod(a, b):
    while b > 0:
        a, b = b, a % b
    return a


def gcd_rec(a, b):
    a -= b
    if a == 0:
        return b
    if a < b:
        a, b = b, a
    return gcd_rec(a, b)


# a, b를 입력받는다
# gcd_sub, gcd_mod, gcd_rec을 각각 호출하여, x, y, z에 리턴값을 저장한다
a, b = map(int, input().split())
if a > b:
    x = gcd_sub(a, b)
    y = gcd_mod(a, b)
    z = gcd_rec(a, b)
else:
    x = gcd_sub(b, a)
    y = gcd_mod(b, a)
    z = gcd_rec(b, a)
print(x, y, z)