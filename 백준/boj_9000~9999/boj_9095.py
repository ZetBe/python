#9095 1, 2, 3 더하기
import sys
input = sys.stdin.readline

t = int(input())
for i in range(t):
    n = int(input())
    dp = [0 for _ in range(n+1)]
    if n == 1:
        print(1)
    elif n == 2:
        print(2)
    elif n == 3:
        print(4)
    else:
        dp[1], dp[2], dp[3] = 1, 2, 4
        for j in range(4, n+1):
            dp[j] = dp[j-1] + dp[j-2] + dp[j-3]
        print(dp[n])