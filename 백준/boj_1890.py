#1890 점프
def move_side(a, b, c):
    if a[b][c]+b < n:
        return a[a[b][c]+b][c]
def move_front(a, b, c):
    if a[b][c]+c < n:
        a[b][a[b][c]+c] = True
        return a[b][a[b][c]+c]

n = int(input())
a = [0 for i in range(n)]

for i in range(n):
    a[i] = list(map(int, input().split()))

dp = [[0 for _ in range(n)] for _ in range(n)]
dp[0][0] = 1
for h in range(n):
    for m in range(n):
        if h == n-1 and m == n-1:
            print(dp[h][m])
        move = a[h][m]
        if h + move < n:
            dp[h+move][m] += dp[h][m]
        if m + move < n:
            dp[h][m+move] += dp[h][m]
