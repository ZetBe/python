#7568 덩치
N = int(input())
x, y = [0 for j in range(N)], [0 for n in range(N)]
a = [1 for m in range(N)]
for i in range(N):
    x[i], y[i] = map(int, input().split())

for b in range(N):
    for h in range(N):
        if (x[b] < x[h] and y[b] < y[h]) and b != h:
            a[b] += 1

for v in range(N):
    print("%d "%a[v], end='')