#11650 좌표 정렬하기
N = int(input())
b = []
for i in range(N):
    a = []
    x, y = map(int, input().split())
    a.append(x)
    a.append(y)
    b.append(a)
b.sort()
for k in range(N):
    print(b[k][0], b[k][1])
