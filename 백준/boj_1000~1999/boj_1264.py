
#1264 모음의 개수
while True:
    a = input()
    b = 0
    if a == '#':
        break
    a = list(a)
    for i in a:
        if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
            b += 1
        elif i == 'A' or i == 'E' or i == 'I' or i == 'O' or i == 'U':
            b += 1
    print(b)