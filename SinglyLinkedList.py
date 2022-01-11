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
        new_node = Node(key)
        new_node.next = self.head
        self.head = new_node
        self.size += 1

    def pushBack(self, key):
        new_node = Node(key)
        v = self.head
        if self.size == 0:
            self.head = new_node
        else:
            while v.next != None:
                v.next
            v.next = new_node
        self.size += 1

    def popFront(self):
        v = self.head
        key = None
        if self.size != 0:
            key = v.key
            self.head = v.next
            self.size -= 1
        return key

    # head 노드의 값 리턴. empty list이면 None 리턴

    def popBack(self):
        front = self.head
        back = None
        backback = None
        if self.size != 0:
            while front != None:
                backback, back, front = back, front, front.next
            if self.head == front:
                self.head = None
            else:
                tail = front
                key = back.key
                backback.next = None

            self.size -= 1
            return key
        else:
            return None

    # tail 노드의 값 리턴. empty list이면 None 리턴

    def search(self, key):
        v = self.head
        sear = False
        while v != None:
            if v.key == key:
                sear = True
                return v
            v = v.next
        if sear == False:
            return None

    # key 값을 저장된 노드 리턴. 없으면 None 리턴

    def remove(self, x):
        v = self.head
        front = v.next
        sear = False
        if v.key == x.key:
            self.head = v.next
            sear = True
            self.size -= 1
            return True
        while front != None:
            if front.key == x.key:
                v.next = front.next
                sear = True
                self.size -= 1
                return True
            v = front
            front = front.next
        if sear == False:
            return sear

    # 노드 x를 제거한 후 True리턴. 제거 실패면 False 리턴

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