#2525 오븐 시계
A, B = map(int, input().split())
C = int(input())
t = B + C
if t >= 60:
    A += t // 60
    t %= 60
    if A >= 24:
        A -= 24
print(A, t)