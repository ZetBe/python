#1920 수 찾기
n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))
c = 0
a.sort()

d = 0
for i in range(m):
    short = 0
    long = len(a) - 1
    while True:
        mid = (long + short)// 2
        if a[mid] == b[i]:
            print(1)
            break
        if a[mid] < b[i]:
            short = mid + 1
        if a[mid] > b[i]:
            long = mid - 1
        if long < short:
            print(0)
            break