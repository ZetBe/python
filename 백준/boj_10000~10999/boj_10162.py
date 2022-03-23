#10162 전자레인지
t = int(input())
a, b, c = 0, 0, 0
if t % 10 != 0:
    t = 5
if t >= 300:
    a = t // 300
    t %= 300
if t < 300 and t >= 60:
    b = t // 60
    t %= 60
if t < 60 and t >= 10:
    c = t // 10

if t == 5:
    print("-1")
else:
    print(a, b, c)