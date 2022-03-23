#10156 과자
k, n, m = map(int, input().split())
price = k*n
price -= m
if price > 0:
    print(price)
else:
    print(0)