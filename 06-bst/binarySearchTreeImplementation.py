class BinarySearchTree:
    #Inner class Node as no Linked List without Node
    class Node:
        def __init__(self, data):
            self.data = data
            self.left = None 
            self.right = None
    
    def __init__(self) -> None:
        self.root = None
    
    def insert(self, data):
        newNode =self.Node(data)
        if self.root is None:
            self.root = newNode
        else:
            currentNode = self.root
            while True:
                if  data < currentNode.data :
                    if currentNode.left is None:
                        currentNode.left = newNode
                        break
                    else:
                        currentNode = currentNode.left
                else :
                    if currentNode.right is None:
                        currentNode.right = newNode
                        break
                    else:
                        currentNode = currentNode.right

    #return node we ask for
    def lookup(self, data):
        #print(data)
        if self.root is None:
            return False
        
        currentNode = self.root
        while (currentNode):
            #print(currentNode.data)
            if data < currentNode.data:
                currentNode = currentNode.left
            elif data > currentNode.data:
                currentNode = currentNode.right
            elif data == currentNode.data:
                return currentNode.data
        return False 

    def traverse(self, node):
        currentNode = node        
        if currentNode.left is not None:
            print(currentNode.data)
            self.traverse(currentNode.left)
        if currentNode.right is not None:
            print(currentNode.data)
            self.traverse(currentNode.right)


tree = BinarySearchTree()
tree.insert(9)
tree.insert(4)
tree.insert(20)
tree.insert(1)
tree.insert(6)
tree.insert(15)
tree.insert(170)
print(tree.lookup(270))
#tree.traverse(tree.root)
#       9
#   4       20
# 1    6  15   170
