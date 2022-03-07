#10039 평균 점수
a = []
for j in range(5):
    c = int(input())
    a.append(c)
b = 0
for i in range(len(a)):
    if a[i] <= 40:
        a[i] = 40
    b += a[i]

b //= 5
print(b)