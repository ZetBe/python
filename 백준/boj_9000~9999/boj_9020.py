#9020 골드바흐 추측
T = int(input())
max = 0
a = []

for i in range(T): #O(N)
    n = int(input())
    a.append(n)
    if a[i] > max:
        max = a[i]

nums = [True] * (max+1)

for k in range(2, max+1):
    for l in range(k*k, max+1, k):
        nums[l] = False

for c in a:
    mini = c
    g = 0
    for j in range(c//2, c+1):
        if nums[j] and nums[c-j]:
            print(c-j, j)
            g = 1
        if g == 1:
            break