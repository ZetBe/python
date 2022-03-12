#1094 막대기
x = int(input())
stick = [64]
while True:
    if x < sum(stick):
        stick[-1] = stick[-1]/2
        stick.append(stick[-1])
        if x <= sum(stick) - stick[-1]:
            stick.pop()
    elif x == sum(stick):
        break
print(len(stick))