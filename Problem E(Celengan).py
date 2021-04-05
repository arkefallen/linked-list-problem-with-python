class Node :

    def __init__(self,data) :
        self.data = data
        self.next = None
    

class LinkedList :

    def __init__(self) :
        self.head = None
        self.tail = None
        self.total = 0
    
    def addTail(self, node) :
        num = Node(node)
        self.total += num.data
        if self.head is None :
            self.head = num
            self.tail = num
        else :
            self.tail.next = num
            self.tail = num
    
    def addHead(self,node) :
        num = Node(node)
        self.total += num.data
        if self.head is None :
            self.head = num
            self.tail = num
        else :
            num.next = self.head
            self.head = num

    def removeHead(self) :
        if self.head is None : 
            print("Linked List Empty !")
        else :
            self.total -= self.head.data
            self.head = self.head.next
            if self.head is self.tail :
                self.tail = None

    def removeTail(self) :
        if self.head is None :
            print("Linked List Empty !")
        elif ( self.head is self.tail ) and self.head is not None :
            self.tail = None
            self.head = None
        else :
            key = self.head
            while key.next.next is not None :
                key = key.next
            self.total -= key.next.data
            key.next = None
            self.tail = key

    def display(self) :
        key = self.head
        if key is None :
            print("Linked List Empty !")
        else :
            while key is not None :
                print(key.data)
                key = key.next

    def peek(self) :
        return self.head.data

celengan = LinkedList()

totalAct = int(input())

acts = []

for element in range(totalAct) :
    acts.append(input().split())

for act in acts :
    if act[0] == '0' :
        celengan.addHead(int(act[1]))
    elif act[0] == '1' :
        celengan.addTail(int(act[1]))
    elif act[0] == '2' :
        celengan.removeHead()
    elif act[0] == '3' :
        celengan.removeTail()

print(celengan.total)