#10886 0 = not cute / 1 = cute
n = int(input())
cute = 0
cute_n = 0
for i in range(n):
    a = int(input())
    if a == 1:
        cute += 1
    else:
        cute_n += 1

if cute > cute_n:
    print("Junhee is cute!")
else:
    print("Junhee is not cute!")