#5086 배수와 약수
while True:
    a, b = map(int, input().split())
    if a == 0 and b == 0:
        break
    if a % b == 0 and b % a != 0:
        print("multiple")
    if b % a == 0 and a % b != 0:
        print("factor")
    if b % a != 0 and a % b != 0:
        print("neither")