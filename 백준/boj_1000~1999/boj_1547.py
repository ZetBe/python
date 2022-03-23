#1547 공
m = int(input())
a = [0, 1, 0, 0]
for i in range(m):
    x, y = map(int, input().split())
    a[x], a[y] = a[y], a[x]

for j in range(4):
    if a[j] == 1:
        print(j)