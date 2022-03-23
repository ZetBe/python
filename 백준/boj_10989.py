#10989 수 정렬하기 3
import sys
input = sys.stdin.readline

n = int(input())
a = [0 for _ in range(10001)]
for i in range(n):
    a[(int(input()))] += 1

for j in range(10001):
    for k in range(a[j]):
        print(j)