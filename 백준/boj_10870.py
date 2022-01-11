#피보나치 수 5 백준
#10870
def fibo(a, b, c, n):
    if n >= 2:
        c = a + b
        a = b
        b = c
        n -= 1
        fibo(a, b, c, n)

    elif n == 1:
        print(c)
        return 0

    elif n == 0:
        print(a)
        return 0

n = int(input())
a = 0
b = 1
c = 1
fibo(a, b, c, n)