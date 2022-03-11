#7682 틱택토
def line(a, x, o, dot):
    n = False
    for i in range(3):
        if a[i] == a[i + 3] == a[i + 6]:
            if x == o and a[i] == 'O' and (dot == 1 or dot == 3):
                n = True
            elif x == o+1 and a[i] == 'X' and (dot == 0 or dot == 2 or dot == 4):
                n = True
    for j in range(3):
        if a[j*3] == a[j*3+1] == a[j*3+2]:
            if x == o and a[j*3] == 'O' and (dot == 1 or dot == 3):
                n = True
            elif x == o+1 and a[j*3] == 'X' and (dot == 0 or dot == 2 or dot == 4):
                n = True
    if a[0] == a[4] == a[8] or a[2] == a[4] == a[6]:
        if x == o and a[4] == 'O' and (dot == 1 or dot == 3):
            n = True
        elif x == o + 1 and a[4] == 'X' and (dot == 0 or dot == 2 or dot == 4):
            n = True
    return n

while True:
    a = input()
    x, o, dot = 0, 0, 0
    xx, oo = 0, 0
    m = 0
    if a == 'end':
        break
    a = list(a)
    for m in a:
        if m == 'X':
            x += 1
        elif m == 'O':
            o += 1
        else:
            dot += 1
    if line(a, x, o, dot) == True:
        print("valid")
    elif line(a, x, o, dot) == False and x == 5 and o == 4:
        print("valid")
    else:
        print("invalid")