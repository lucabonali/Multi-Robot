from Node import *
from Path import *

class Agent():
    def __init__(self,position,targets):
        self.targetString = "T"
        self.wallString = "#"
        self.toExpand = []
        self.targets = targets
        self.position = position
        self.path = []

    def getListOfPosition(self,mapChar):
        list = []
        for i in range(len(mapChar)):
            for j in range(len(mapChar[i])):
                list.append((i, j))
        return list

    def constructTree(self,mapChar, node):
        if self.checkTarget(node):
            print("Target Found:", node)
            return node
        else:
            self.toExpand.append(node)
            listPosition = self.getListOfPosition(mapChar)
            return self.expand(node, listPosition, mapChar)

    def available(self,listPosition, coord):
        for i in range(len(listPosition)):
            if listPosition[i] == coord:
                listPosition.remove(coord)
                return True
        return False

    def expand(self, node, listPosition, mapChar):
        self.toExpand.remove(node)
        for i in range(len(node.adjacents)):
            xCoord = node.adjacents[i][0]
            yCoord = node.adjacents[i][1]
            if self.available(listPosition, coord=(xCoord,yCoord)):
                try:
                    value = mapChar[xCoord][yCoord]
                    if not value == self.wallString:
                        child = Node(father=node, xCoord=xCoord, yCoord=yCoord, value=value)
                        node.addChildren(child)
                        self.toExpand.append(child)
                except:
                    pass
        for i in range(len(node.children)):
            if self.checkTarget(node.children[i]):
                self.toExpand.clear()
                return node.children[i]
        if not len(self.toExpand) == 0:
            return self.expand(self.toExpand[0], listPosition, mapChar)

    def checkTarget(self,node):
        if node.value == self.targetString:
            return True
        return False

    def constructPath(self,node, path):
        if node == None:
            return path
        path.addNode(node)
        return self.constructPath(node.father, path)
