class StackDemo:
    #Inner class Node as no Linked List without Node
    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None 

    def __init__(self) -> None:
        self.top = None
        self.bottom = None
        self.length = 0

    def peek(self):
        if self.length > 0:
            return self.top.data
        else:
            return None

    def push(self, data):        
        newNode = self.Node(data)
        if self.length == 0:
            self.top = newNode
            self.bottom = newNode
            self.length = 1
        else:
            holdingNode = self.top
            self.top = newNode
            self.top.next = holdingNode
            self.bottom = holdingNode
            self.length += 1
        

    def pop(self):
        if self.length == 0:
            return None
        else:
            holdingNode = self.top
            self.top = self.top.next
            self.length -= 1
            return holdingNode.data

myStack = StackDemo()
myStack.push('google')
myStack.push('udemy')
myStack.push('youtube')
print(myStack.peek())
print(myStack.pop())