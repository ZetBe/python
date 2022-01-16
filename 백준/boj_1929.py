#1929 소수 구하기
M, N = map(int, input().split())
num = [True] * (N+1)
num[1] = False
for i in range(2, N+1):
    for j in range(2*i, N+1, i):
        num[j] = False

for n in range(M, N + 1):
    if num[n]:
        print(n)
