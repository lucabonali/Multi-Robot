from Node import *
from Path import *
import threading


class Agent():
    def __init__(self,position,targets, agentNode, mapChar):
        self.targetString = "T"
        self.wallString = "#"
        self.toExpand = []
        self.targets = targets
        self.position = position
        self.path = Path()
        self.agentNode = agentNode
        self.mapChar = mapChar
        self.objNode = None

    def run(self):
        t = threading.Thread(target=self.constructTree())
        t.start()

    def constructTree(self):
        if self.checkTarget(self.agentNode):
            print("Target Found:", self.agentNode)
            self.objNode = self.agentNode
        else:
            self.toExpand.append(self.agentNode)
            self.setHeuristic(self.agentNode)
            listPosition = self.getListOfPosition(self.mapChar)
            self.expand(self.agentNode, listPosition, self.mapChar)
            self.path = self.constructPath(self.objNode, self.path)
            self.path.path.reverse()
            self.path.toString()

    def getListOfPosition(self,mapChar):
        list = []
        for i in range(len(mapChar)):
            for j in range(len(mapChar[i])):
                list.append((i, j))
        return list

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
                        self.setHeuristic(child)
                        self.updateFrontier(child)
                        #self.toExpand.append(child)
                except:
                    pass
        for i in range(len(node.children)):
            if self.checkTarget(node.children[i]):
                self.toExpand.clear()
                self.objNode = node.children[i]
        if not len(self.toExpand) == 0:
            self.expand(self.toExpand[0], listPosition, mapChar)

    def available(self,listPosition, coord):
        for i in range(len(listPosition)):
            if listPosition[i] == coord:
                listPosition.remove(coord)
                return True
        return False

    def checkTarget(self,node):
        if node.value == self.targetString:
            return True
        return False

    def constructPath(self,node, path):
        if node == None:
            return path
        if not (node.value == "R"):
            path.addNode(node)
        return self.constructPath(node.father, path)

    def setHeuristic(self, node):
        heuristic = self.getNearTarget(node.xCoord, node.yCoord)
        node.heuristic = heuristic

    def getNearTarget(self,x,y):
        nearValues = []
        for i in range(len(self.targets)):
            nearValues.append(abs((self.targets[i][0]-x)+(self.targets[i][1]-y)))
        nearValues.sort()
        return nearValues[0]

    def updateFrontier(self, child):
        h = child.heuristic
        for i in range(len(self.toExpand)):
            if self.toExpand[i].heuristic >= h:
                self.toExpand.insert(i+5,child)
                return
        self.toExpand.append(child)