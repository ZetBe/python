#2579 계단 오르기
import sys
input = sys.stdin.readline

n = int(input())
a = []
count = 0
for i in range(n):
    a.append(int(input()))
first = []


first.append(max(a[0]+a[2], a[1]+a[2]))
if n == 1:
    first.append(a[0])
    print(a[0])
    exit()
elif n == 2:
    first.append(a[0])
    first.append(a[0] + a[1])
    print(a[0]+a[1])
    exit()
else:
    first.append(a[0])
    first.append(a[0]+a[1])
    first.append(max(a[0] + a[2], a[1] + a[2]))
    for j in range(3, n):
        first.append(max(first[j-2]+a[j], first[j-3]+a[j-1]+a[j]))


print(max(first))