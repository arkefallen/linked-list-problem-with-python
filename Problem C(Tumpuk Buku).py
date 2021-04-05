class Book :

    def __init__(self,code=None,name=None) :
        self.next = None
        self.name = name
        self.code = code
    
class Stack :

    def __init__(self) :
        self.head = None
        self.tail = None
    
    def push(self, code,name) :
        book = Book(code,name)
        if self.head is None :
            self.head = book
            self.tail = book
        else :
            self.tail.next = book
            self.tail = book

    def pop(self) :
        if self.head is None :
            print("Linked List Empty !")
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
        return self.tail

bookStack = Stack()

totalActs = int(input())

acts = []

for act in range(totalActs) :
    acts.append(input().split())

for act in acts :
    if act[0] == 'T' :
        bookStack.push(act[1],act[2])
    if act[0] == 'A' :
        bookStack.pop()

while bookStack.head != None :
    print(bookStack.peek().code,bookStack.peek().name)
    bookStack.pop()