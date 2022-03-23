#2805 나무 자르기
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
a = list(map(int, input().split()))
right = max(a)
left = 0
while left <= right:
    count = 0
    mid = (right + left) // 2
    for j in a:
        if j > mid:
            count += j - mid
    if count >= m:
        left = mid + 1
    else:
        right = mid - 1
print(left-1)