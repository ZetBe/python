#5217 쌍의 합
t = int(input())
for i in range(t):
    n = int(input())
    a = 0
    x, y = 1, n-1
    print("Pairs for {}: ".format(n), end='')
    while x < y:
        if a > 0 :
            print(", ", end='')
        print("{} {}".format(x, y), end='')
        x += 1
        y -= 1
        a += 1
    print()