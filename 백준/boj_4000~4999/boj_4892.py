#4892 숫자 맞추기 게임
i = 0
while True:
    i += 1
    n = int(input())
    if n == 0:
        break
    a = 3*n
    if a % 2 == 1:
        b = (a+1)/2
    else:
        b = a/2
    c = b*3
    d = c // 9
    if a % 2 == 1:
        print("{}. odd {}".format(i, int(d)))
    else:
        print("{}. even {}".format(i, int(d)))