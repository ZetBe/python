#10102 개표
v = int(input())
vote = input()
vote = list(vote)
a, b = 0, 0
for i in range(v):
    if vote[i] == 'A':
        a += 1
    elif vote[i] == 'B':
        b += 1
if a > b:
    print("A")
elif a == b:
    print("Tie")
else:
    print("B")