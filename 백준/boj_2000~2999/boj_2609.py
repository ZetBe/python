#2609 최대공약수와 최소공배수
import sys
input = sys.stdin.readline

a, b = map(int, input().split())
aa, bb = a, b
while a != 0 and b != 0:
    if a > b:
        a %= b
    else:
        b %= a
if a > b:
    print(a)
    print(aa*bb//a)
else:
    print(b)
    print(bb*aa//b)