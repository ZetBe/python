#3035 스캐너
import sys
input = sys.stdin.readline

r, c, zr, zc = map(int, input().split())
a = [0 for _ in range(r)]
for i in range(r):
    a[i] = list(input())

for b in range(r):
    for d in range(zr):
        for q in range(c):
            for p in range(zc):
                print(a[b][q], end='')
        print()