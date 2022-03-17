#11051 이항 계수 2
n, k = map(int, input().split())
nn, kk, nk = n, k, n-k
summ = 1
summ_1 = 1
summ_2 = 1
while nn != 1:
    summ *= nn
    nn -= 1
    if kk > 1:
        summ_1 *= kk
        kk -= 1
    if nk > 1:
        summ_2 *= nk
        nk -= 1
summ //= summ_1 * summ_2
print(summ % 10007)