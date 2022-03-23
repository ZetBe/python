#11651 좌표 정렬하기2
N = int(input())
b = []
for i in range(N):
    a = []
    x, y = map(int, input().split())
    a.append(y)
    a.append(x)
    b.append(a)
b.sort()
for k in range(N):
    print(b[k][1], b[k][0])
