#7682 틱택토
def o_line(a, x, o, dot):
    n = False
    for i in range(3):
        if a[i] == a[i + 3] == a[i + 6] == 'O':
            n = True

    for j in range(3):
        if a[j*3] == a[j*3+1] == a[j*3+2] == 'O':
            n = True

    if (a[0] == a[4] == a[8] == 'O') or (a[2] == a[4] == a[6] == 'O'):
        n = True

    return n

def x_line(a, x, o, dot):
    n = False
    for i in range(3):
        if a[i] == a[i + 3] == a[i + 6] == 'X':
            n = True
    for j in range(3):
        if a[j * 3] == a[j * 3 + 1] == a[j * 3 + 2] == 'X':
            n = True
    if (a[0] == a[4] == a[8] == 'X') or (a[2] == a[4] == a[6] == 'X'):
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
    if o_line(a, x, o, dot) == True and x_line(a, x, o, dot) == False and x == o:
        print("valid")
    elif o_line(a, x, o, dot) == False and x_line(a, x, o, dot) == True and x == o+1:
        print("valid")
    elif o_line(a, x, o, dot) == False and x == 5 and o == 4 and x_line(a, x, o, dot) == False:
        print("valid")
    else:
        print("invalid")