#1436 영화감독 숌
import math
N = int(input())
b = []
c = 0
a = 666
while True:
    d = a
    for j in range(int(math.log10(a))-1):
        if d % 1000 == 666:
            b.append(a)
            break
        d //= 10
    if len(b) == N:
        break
    a += 1

print(b[N-1])