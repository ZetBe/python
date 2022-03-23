#3079 입국심사
#이분 탐색 *중요*
import sys
input = sys.stdin.readline


n, m = map(int, input().split())
check = [int(input()) for i in range(n)]

answ = 0
left = 0
right = m * max(check)
while left <= right:
    middle = (left + right) // 2
    count = 0
    for j in check:
        count += middle // j
    if count >= m:
        answ = middle
        right = middle - 1
    else:
        left = middle + 1
print(answ)