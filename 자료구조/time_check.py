import time, random


def sum(A, n):
    x = int()
    b = []
    for i in range(n):
        line = []
        for j in range(i, n):
            line.append(x)
            x = 0
            for z in range(i, n):
                x += A[z]
        b.append(line)


# code here

# n = 1 이상 5000 이하 정수 값 입력
# 리스트 A에 랜덤 정수 값 n개 채움
# sum 함수 호출 + 시간 측정
# 함수의 수행시간을 출력
A = []
n = int(input())
start = time.time() * 100
for a in range(n):
    A.append(random.randint(0, 100))
b = sum(A, n)
print(time.time() * 100 - start)