#팩토리얼 백준
#10872
def a(N, sum):
    if N == 0:
       print(sum)
       return 0
    else:
        sum *= N
        a(N-1, sum)

N = int(input())
sum = 1
a(N, sum)