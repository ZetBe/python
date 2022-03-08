#1920 수 찾기
n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))
c = 0
a.sort()
print(a)
for i in range(m):
    for j in range(n):
        if a[j] == b[i]:
            print(1)

        if a[j] > b[i]:
            print(0)
            break
