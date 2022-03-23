N = list(map(int, input().split()))
Sum = 0
Max = 0
A = list(map(int, input().split()))

for j in range(N[0]-2):
    for n in range(j+1, N[0]-1):
        for m in range(n+1, N[0]):
            Sum = A[j] + A[n] + A[m]
            if Sum <= N[1] and Max <= Sum:
                Max = Sum
            Sum = 0

print(Max)