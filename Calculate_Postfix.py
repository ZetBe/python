class Stack:
    def __init__(self):
        self.items = []  # 데이터 저장을 위한 리스트 준비

    def push(self, val):
        self.items.append(val)

    def pop(self):
        try:  # pop할 아이템이 없으면
            return self.items.pop()
        except IndexError:  # indexError 발생
            print("Stack is empty")

    def top(self):
        try:
            return self.items[-1]
        except IndexError:
            print("Stack is empty")

    def __len__(self):  # len()로 호출하면 stack의 item 수 반환
        return len(self.items)

    def isEmpty(self):
        return self.__len__() == 0


def compute_postfix(postfix):
    S = Stack()
    value = float(0)
    value1 = float(0)
    post = postfix.split(" ")
    for i in post:
        if i == '+':
            value = S.pop()
            value += S.pop()
            S.push(value)
            value = float(0)

        elif i == '-':
            value -= S.pop()
            value += S.pop()
            S.push(value)
            value = float(0)

        elif i == '*':
            value = S.pop()
            value *= S.pop()
            S.push(value)
            value = float(0)

        elif i == '/':
            value = S.pop()
            value1 = S.pop()
            value1 = value1 / value
            S.push(value1)
            value = float(0)
            value1 = float(0)

        elif i == '^':
            value = S.pop()
            value1 = S.pop()
            value1 ^= value
            S.push(value1)
            value = float(0)
            value1 = float(0)

        else:
            z = float(i)
            S.push(z)

    return float(S.pop())


postfix = input()
val = float(compute_postfix(postfix))
print("{:.4f}".format(val))