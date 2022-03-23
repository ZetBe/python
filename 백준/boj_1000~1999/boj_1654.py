#1654 랜선 자르기
import sys
input = sys.stdin.readline
k, n = map(int, input().split())
a = []
for i in range(k):
    a.append(int(input()))

left, right = 1, max(a)
while left <= right:
    mid = (left+right)//2
    count = 0
    for j in a:
        count += j // mid
    if count >= n:
        left = mid +1
    else:
        right = mid -1

print(left -1)