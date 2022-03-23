#12865 평범한 배낭
#냅색 알고리즘 *중요*
n, k = map(int, input().split())
m = 0
val = 0
max_val = 0
w, v = [], []
for _ in range(n):
    a = list(map(int, input().split()))
    w.append(a[0])
    v.append(a[1])
dp = [[0 for x in range(k+1)] for x in range(n+1)]
for i in range(n+1):
    for j in range(k+1):
        if i == 0 or j == 0:
            m = 0
        elif j - w[i-1] >= 0:
            dp[i][j] = max(dp[i-1][j-w[i-1]]+v[i-1], dp[i-1][j])
        else:
            dp[i][j] = dp[i-1][j]
print(dp[n][k])