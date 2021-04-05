def createStack() :
    stack = []
    return stack

def push(stack,data) :
    stack.append(data)

def pop(stack) :
    if isEmpty(stack) == False :
        # Jika head berada di depan list
        return stack.pop()
        # Jika head berada di belakang list
        # stack.pop(0)
    else :
        return "Stack Empty !"
        
def peek(stack) :
    # Jika head berada di depan list
    return stack[-1]
    # Jika head berada di belakang list
    # return stack[0]

def isEmpty(stack) :
    if len(stack) == 0 :
        return True
    else :
        return False

def display(stack) :
    while isEmpty(stack) == False :
        print(pop(stack))


jmlMhs = int(input())
nilaiMhs = input().split()

studScore = list(map(int, nilaiMhs))

stack = createStack()

for element in studScore :
    if element < 0 or element > 100 :
        continue
    else :
        push(stack,element)

display(stack)