#11656 접미사 배열
s = list(input())
a = []
b = ""
for i in range(len(s)):
    b = ""
    for j in range(i, len(s)):
        b += s[j]
    a.append(b)
a.sort()
for i in range(len(a)):
    print(a[i])