#1789 수들의 합
s = int(input())
N = 1
N_ = 1
while s >= N_:
    N += 1
    N_ += N

print(N-1)