#Create an Undirected Unweighted graph 
#Represented with Adjacent List
class Graph:
    def __init__(self) -> None:
        self.numOfNodes = 0
        self.adjacentList = {}

    def addVertex(self, node):
        self.adjacentList[node] = []
        self.numOfNodes += 1

    def addEdge(self, node1, node2):
        listLength = len(self.adjacentList[node1])
        print(self.adjacentList)
        #self.adjacentList[node1][listLength] = [node2] 
        self.adjacentList.update()

    def showConnections(self):
        if self.numOfNodes > 0:
            for i in self.numOfNodes + 1:
                if len(self.adjacentList[i]) > 1:
                    for j in len(self.adjacentList[i]) - 1:
                        print(self.adjacentList[i][j])
        return None

myGraph = Graph()
myGraph.addVertex(0)
myGraph.addVertex(1)
myGraph.addVertex(2)
myGraph.addVertex(3)
myGraph.addVertex(3)
myGraph.addVertex(3)
myGraph.addVertex(3)
myGraph.addEdge(3,1)
myGraph.addEdge(3,4)
myGraph.addEdge(4,2)
myGraph.addEdge(4,5)
myGraph.addEdge(1,2)
myGraph.addEdge(1,0)
myGraph.addEdge(0,2)
myGraph.addEdge(6,5)
myGraph.showConnections()