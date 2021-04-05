class Node :

    def __init__(self,data) :
        self.next = None
        self.data = data
    
class Stack :

    def __init__(self) :
        self.head = None
        self.tail = None
    
    def push(self, node) :
        data = Node(node)
        if self.head is None :
            self.head = data
            self.tail = data
        else :
            self.tail.next = data
            self.tail = data

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

    def display(self) :
        key = self.head
        stackList = []
        while key is not None :
            stackList.append(str(key.data))
            key = key.next
        result = ''.join(stackList)
        print(result,end='')

    def peek(self) :
        return self.tail.data

num = int(input())
stack = Stack()

while num != 0 :
    stack.push(num%2)
    if num != 0 :
        num//=2
    else :
        stack.push(num)

stack.display()

# stackList = []

# while stack.head != None :
#     stackList.append(str(stack.peek()))
#     stack.pop()

# result = ''.join(stackList)

# print(result,end='')
