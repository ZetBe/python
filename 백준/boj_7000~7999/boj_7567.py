#7567 그릇
a = input()
a = list(a)
long = 0
for i in range(len(a)):
    if i == 0:
        long += 10
    else:
        if a[i-1] == a[i]:
            long += 5
        else:
            long += 10
print(long)