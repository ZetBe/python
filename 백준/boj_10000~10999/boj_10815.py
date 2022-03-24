#10815 숫자 카드
import sys
input = sys.stdin.readline

n = int(input())
a = [0 for _ in range(20000001)]
b = list(map(int, input().split()))
for j in b:
    a[j+10000000] += 1
m = int(input())
c = list(map(int, input().split()))
for i in c:
    a[i+10000000] += 1
for k in c:
    if a[k+10000000] >= 2:
        print("1 ", end='')
    else:
        print("0 ", end='')