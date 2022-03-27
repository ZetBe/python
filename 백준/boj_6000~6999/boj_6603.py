#6603 로또
import sys, itertools
input = sys.stdin.readline

while True:
    b = list(map(int, input().split()))
    if b[0] == 0:
        break
    b[0], b[len(b)-1] = b[len(b)-1], b[0]
    b.pop()
    b.sort()
    c = itertools.combinations(b, 6)
    for i in c:
        for j in i:
            print("%d "%(j), end='')
        print()
    print()