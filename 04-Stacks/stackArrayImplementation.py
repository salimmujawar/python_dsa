class StackDemo:   
    def __init__(self) -> None:
        self.array = []

    def peek(self):
        return self.array[len(self.array-1)]        

    def push(self, data):         
        self.array.push(data)

    def pop(self):
        return self.array.pop()

myStack = StackDemo()
myStack.push('google')
myStack.push('udemy')
myStack.push('youtube')
print(myStack.peek())
print(myStack.pop())