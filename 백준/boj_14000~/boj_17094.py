#17094 Serious Problem
import sys
input = sys.stdin.readline

n = int(input())
s = list(input())
two, eee = 0, 0
for i in range(n):
    if s[i] == '2':
        two += 1
    elif s[i] == 'e':
        eee += 1
if two > eee:
    print(2)
elif two < eee:
    print("e")
else:
    print("yee")