class Queue:
    #Inner class Node as no Linked List without Node
    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None 

    def __init__(self) -> None:
        self.first = None
        self.last = None
        self.length = 0        

    def peek(self):
        return self.first.data

    def enqeue(self, data):
        newNode = self.Node(data)
        if self.length == 0:
            self.first = newNode
            self.last = self.first
        else:
            self.last.next = newNode
            self.last = newNode
        self.length += 1

    def dequeue(self):
        if self.length == 0:
            return None
        else:
            holdingNode = self.first
            self.first = self.first.next
            self.length -= 1
            return holdingNode.data

myQueue = Queue()
myQueue.enqeue("Saba")
myQueue.enqeue("Salim")
myQueue.enqeue("Sana")
print(myQueue.peek())
print(myQueue.dequeue())
print(myQueue.dequeue())