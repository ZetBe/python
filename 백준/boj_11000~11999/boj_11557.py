#11557 Yangjojang of The Year
t = int(input())
for i in range(t):
    n = int(input())
    ss, ll = [], []
    max_l = 0
    for j in range(n):
        s, l = input().split()
        ss.append(s)
        ll.append(int(l))
        if max_l < ll[j]:
            max_l = ll[j]
            max_s = ss[j]
    print(max_s)