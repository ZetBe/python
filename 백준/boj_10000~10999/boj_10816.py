#10816 숫자 카드 2
import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))
c = [0 for _ in range(20000001)]
for i in range(n):
    c[a[i]+10000000] += 1
for k in b:
    print("%d "%(c[k+10000000]), end='')