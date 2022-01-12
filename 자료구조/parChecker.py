class deque:
    def __init__(self, s):
        self.items = list(s)  # 데이터 저장을 위한 리스트 준비
        self.front_index = 0  # 다음 dequeue될 값의 인덱스 저장

    def append(self, val):
        self.items.append(val)

    def appendleft(self, val):
        self.items.insert(0, val)

    def pop(self):
        z = self.items[-1]
        del self.items[-1]
        return z

    def popleft(self):
        x = self.items[0]
        del self.items[0]
        return x

    def left(self):
        return self.items[0]

    def right(self):
        return self.items[-1]

    def __len__(self):  # len()로 호출하면 stack의 item 수 반환
        return len(self.items)  # why?


def check_palindrome(s):
    dq = deque(s)
    palindrome = True
    while len(dq) > 1:
        if dq.popleft() != dq.pop():
            palindrome = False
            break
    return palindrome


palindrome = input()
pal = check_palindrome(palindrome)
print(pal)