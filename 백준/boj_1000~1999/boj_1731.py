#1731 추론
import sys
input = sys.stdin.readline

n = int(input())
a = []
for i in range(n):
    a.append(int(input()))
if a[1] - a[0] == a[2] - a[1]:
    a.append(a[len(a)-1]+a[1]-a[0])
elif a[1] // a[0] == a[2] // a[1]:
    a.append(a[len(a)-1]*(a[1]//a[0]))
print(a[len(a)-1])