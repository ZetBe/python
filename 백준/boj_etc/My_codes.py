#1371 가장 많은 글자
import sys
a = [0 for j in range(26)]
while True:
    n = list(sys.stdin.readline())
    if not(n):
        break
    for i in n:
        if ord(i) >= 97 and ord(i) <= 122:
            a[ord(i)-97] += 1
for j in range(26):
    if a[j] == max(a):
        print(chr(j+97), end='')
