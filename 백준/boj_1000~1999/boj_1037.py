#1037 약수
import sys
input = sys.stdin.readline

num_n = int(input())
a = list(map(int, input().split()))
if num_n == 1:
    a[0] = a[0]**2
    print(a[0])
else:
    a.sort()
    print(a[0]*a[len(a)-1])