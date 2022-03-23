# 나머지 코드
def pushFront(self, x):
    v = Node(x)
    z = self.head.next
    v.next = z
    v.prev = self.head
    z.prev = v
    self.head.next = v


def pushBack(self, x):
    v = self.head.next
    z = Node(x)
    if v == None:
        self.head.next = z
        z.prev = self.head
        z.next = self.head
    else:
        tail = self.head.next
        while tail.next != self.head:
            tail = tail.next
        tail.next = z
        z.next = self.head
        z.prev = tail


def popFront(self):
    v = self.head.next
    if v.next == self.head:
        z = self.head
    else:
        z = v.next
    z.prev = self.head
    self.head.next = z
    return v


def popBack(self):
    v, z = self.head.next, v.next
    if z == self.head:
        self.head.next = self.head
        self.head.prev = self.head
        return v
    else:
        while z != self.head:
            v, z = v.next, z.next
        z.prev = v.prev
        v.prev.next = z
        return v


def search(self, x):
    v = self.head.next
    while v.key != x and v != self.head:
        v = v.next
    if v.key == x:
        return v
    if v == self.head:
        return None


def insertAfter(self, x, cmd):
    c = Node(cmd)
    x.prev.next = c
    c.next = x
    c.prev = x.prev
    x.prev = c


def insertBefore(self, x, cmd):
    c = Node(cmd)
    x.next.prev = c
    c.prev = x
    c.next = x.next
    x.next = c


def first(self):
    v = self.head.next.key
    return v


def last(self):
    v = self.head.next
    while v.next != self.head:
        v = v.next
    return v.key


def deleteNode(self, x):
    x.next.prev = x.prev
    x.prev.next = x.next


def splice(self, a, b, x):  # cut [a..b] after x
    if a == None or b == None or x == None:
        return
    a.prev.next = b.next  # 1. [a..b] 구간을 잘라내기
    b.next.prev = a.prev
    x.next.prev = b  # 2. [a..b]를 x 다음에 삽입하기
    b.next = x.next
    a.prev = x
    x.next = a


def moveAfter(self):
    def moveBefore(self):

        def isEmpty(self):