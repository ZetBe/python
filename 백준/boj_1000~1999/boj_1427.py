#1427 소트인사이드
import sys
input = sys.stdin.readline

n = list(input())
n.pop()
n = list(map(int, n))
n.sort(reverse=True)
for i in n:
    print(i, end='')