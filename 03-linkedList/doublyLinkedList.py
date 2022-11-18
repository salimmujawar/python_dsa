#Implememtation of Linked List
class LinkedList:
    #Inner class Node as no Linked List without Node
    class Node:
        def __init__(self, data):
            self.pre = None 
            self.data = data
            self.next = None 
            
    
    def __init__(self, data):
        self.head = self.Node(data)
        self.tail = self.head
        self.length = 1
    
    def show(self):
        node = self.head
        while node is not None:
            print(node.data)
            node = node.next

    def append(self, data):
        newNode = self.Node(data)
        self.tail.next = newNode
        self.tail = newNode
        self.length += 1

    def prepend(self, data):
        newNode = self.Node(data)
        newNode.next = self.head
        self.head = newNode
        self.length += 1

    def remove(self, index):
        #check params, +ve in range
        #find the pre node
        preNode = self.traverseToIndex(index - 1)
        unwantedNode = preNode.next
        preNode.next = unwantedNode.next
        self.length -= 1
    
    def insert(self, index, data):
        #check params
        if index <= self.length:
            #put it in the last
            self.append(data)
            return
        newNode = self.Node(data)
        preNode = self.traverseToIndex(index - 1)
        newNode.next = preNode.next
        preNode.next = newNode
        self.length += 1
        return

    def traverseToIndex(self, index):
        i = 1
        node = self.head
        while i != index:
            node = node.next
            i += 1
        return node

linkedList = LinkedList(10)
# linkedList.append(5)
# linkedList.prepend(16)
# linkedList.insert(3, 40)
print(linkedList.show())
# print(linkedList.length)
# linkedList.remove(2)
# print(linkedList.show())
# print(linkedList.length)
    

