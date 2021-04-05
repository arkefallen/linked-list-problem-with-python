class Node :

    def __init__(self,data=None) :
        self.next = None
        self.data = data
    
class Stack :

    def __init__(self) :
        self.head = None
        self.tail = None
    
    def push(self,node) :
        data = Node(node)
        if self.head is None :
            self.head = data
            self.tail = data
        else :
            self.tail.next = data
            self.tail = data
    
    def pop(self) :
        if self.head == None : 
            return
        elif ( self.head is self.tail ) and self.head is not None :
            self.tail = None
            self.head = None
        else :
            key = self.head
            while key.next.next is not None :
                key = key.next
            key.next = None
            self.tail = key

    def peek(self) :
        return self.tail.data

    def display(self) :
        key = self.head
        print("[ ",end='')
        while key != None :
            print(key.data,end=' ')
            key = key.next
        print("]")

powerStack = Stack()

totalActs = int(input())

acts = []

for act in range(totalActs) :
    acts.append(input().split())

for act in acts :
    if act[0] == "PUSH" :
        powerStack.push(act[1])
        powerStack.display()
    elif act[0] == "POP" :
        if powerStack.head != None :
            powerStack.pop()
            powerStack.display()
        else :
            print("ERROR : STACK KOSONG")
            powerStack.pop()
    elif act[0] == "POWPUSH" :
        for i in range(int(act[1])) :
            powerStack.push(act[2])
        powerStack.display()
    elif act[0] == "POWPOP" :
        for element in range(int(act[1])) :
            if powerStack.head != None :
                powerStack.pop()
            else :
                break
