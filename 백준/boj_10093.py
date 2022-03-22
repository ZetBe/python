#10093 숫자
import sys
input = sys.stdin.readline

a, b = map(int, input().split())
if b > a:
    print(b-a-1)
    for i in range(a + 1, b):
        print("{} ".format(i), end='')
elif a > b:
    print(a-b-1)
    for i in range(b + 1, a):
        print("{} ".format(i), end='')
else:
    print(0)
    print("")