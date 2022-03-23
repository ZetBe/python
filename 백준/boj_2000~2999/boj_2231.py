#2231 분해합
N = int(input())
Sum = 0

for i in range(N):
    Num = i
    Sum = i + i % 10
    Num //= 10
    while Num > 0:
        Sum += Num % 10
        Num //= 10
    if Sum == N:
        print(i)
        break
    else:
        Sum = 0
    if i == N-1:
        print(0)