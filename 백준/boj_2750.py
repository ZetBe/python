import sys
N = int(input())
if N <= 0:
    sys.exit()
a = [0 for j in range(N)]
for i in range(N):
    a[i] = int(input())
a.sort()
for m in range(N):
    print(a[m])