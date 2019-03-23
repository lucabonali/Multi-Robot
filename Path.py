class Path():
    def __init__(self):
        self.path = []
        self.len = 0
        self.solution = False

    def addNode(self, node):
        self.path.append(node)
        self.len += 1

    def removeNode(self, node):
        self.path.remove(node)

    def toString(self):
        for i in range(len(self.path)):
            if not self.path[i] is None:
                print(i,"Node:",self.path[i].xCoord,self.path[i].yCoord)