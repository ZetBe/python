#4562 No Brainer
n = int(input())
for i in range(n):
    x, y = map(int, input().split())
    if x < y:
        print("NO BRAINS")
    elif x >= y:
        print("MMM BRAINS")