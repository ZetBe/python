#2751 수 정렬하기 2
import sys
input = sys.stdin.readline

n = int(input())
a = []
for i in range(n):
    a.append(int(input()))
a.sort()
for j in range(n):
    print(a[j])