class Node:
    def __init__(self, key=None):
        self.key = key
        self.next = None

    def __str__(self):
        return str(self.key)


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def __len__(self):
        return self.size

    def printList(self):  # 변경없이 사용할 것!
        v = self.head
        while (v):
            print(v.key, "->", end=" ")
            v = v.next
        print("None")

    def pushFront(self, key):
        new = Node(key)
        new.next = self.head
        self.head = new
        self.size += 1

    def pushBack(self, key):
        new = Node(key)
        if self.size == 0:
            self.head = new

        else:
            tail = self.head
            while tail.next != None:
                tail = tail.next
            tail.next = new
        self.size += 1

    def popFront(self):
        now = None
        if len(self) > 0:
            now = self.head.key
            self.head = self.head.next
            self.size -= 1
        return now

    def popBack(self):  # tail 노드의 값 리턴. empty list이면 None 리턴
        pre, tail = None, None
        if len(self) > 0:
            pre, tail = None, self.head
            if len(self) > 1:
                while tail.next != None:
                    pre, tail = tail, tail.next
            key = tail.key
            if self.head == tail:
                self.head = None
            else:
                pre.next = tail.next
            self.size -= 1
            return key
        else:
            return None

    def search(self, key):  # key 값을 저장된 노드 리턴. 없으면 None 리턴
        v = self.head
        if len(self) == 0:
            return None
        while v != None:
            if v.key == key:
                return v
                break
            v = v.next
        return None

    def remove(self, x):  # 노드 x를 제거한 후 True리턴. 제거 실패면 False 리턴
        v = self.head.next
        pre = self.head
        if x.key == None:
            return False
        if self.head == None:
            return False
        if pre.key == x.key:
            if len(self) > 1:
                self.head = self.head.next
            else:
                self.head = None
            self.size -= 1
            return True
        while v.next != None:
            if v.key == x.key:
                pre.next = v.next
                self.size -= 1
                return True
            v, pre = v.next, v
        return False

    def size(self):
        return self.size


# 아래 코드는 수정하지 마세요!
L = SinglyLinkedList()
while True:
    cmd = input().split()
    if cmd[0] == "pushFront":
        L.pushFront(int(cmd[1]))
        print(int(cmd[1]), "is pushed at front.")
    elif cmd[0] == "pushBack":
        L.pushBack(int(cmd[1]))
        print(int(cmd[1]), "is pushed at back.")
    elif cmd[0] == "popFront":
        x = L.popFront()
        if x == None:
            print("List is empty.")
        else:
            print(x, "is popped from front.")
    elif cmd[0] == "popBack":
        x = L.popBack()
        if x == None:
            print("List is empty.")
        else:
            print(x, "is popped from back.")
    elif cmd[0] == "search":
        x = L.search(int(cmd[1]))
        if x == None:
            print(int(cmd[1]), "is not found!")
        else:
            print(int(cmd[1]), "is found!")
    elif cmd[0] == "remove":
        x = L.search(int(cmd[1]))
        if L.remove(x):
            print(x.key, "is removed.")
        else:
            print("Key is not removed for some reason.")
    elif cmd[0] == "printList":
        L.printList()
    elif cmd[0] == "size":
        print("list has", len(L), "nodes.")
    elif cmd[0] == "exit":
        print("DONE!")
        break
    else:
        print("Not allowed operation! Enter a legal one!")