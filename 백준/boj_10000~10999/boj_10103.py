#10103 주사위 게임
n = int(input())
c, s = 100, 100
for i in range(n):
    cy, sd = map(int, input().split())
    if cy > sd:
        s -= cy
    if cy < sd:
        c -= sd

print(c)
print(s)