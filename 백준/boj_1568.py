#1568 새
import sys
input = sys.stdin.readline

n = int(input())
i = 1
count = 0
while n != 0:
    if n < i:
        i = 1
    n -= i
    i += 1
    count += 1

print(count)