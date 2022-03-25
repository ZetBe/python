#10867 중복 빼고 정렬하기
import sys
input = sys.stdin.readline

n = int(input())
a = [0 for _ in range(2001)]
b = list(map(int, input().split()))
for i in range(n):
    a[b[i]+1000] += 1
for j in range(2001):
    if a[j] > 0:
        print("%d "%(j-1000), end='')