from mesa import Agent
from Bid import Bid
from Node import *
from Path import *
import threading


class RoutingAgent(Agent):
    def __init__(self,unique_id, model,nRobots,position,targets, agentNode, mapChar):
        super().__init__(unique_id, model)
        self.targetString = "T"
        self.wallString = "#"
        self.nRobots = nRobots
        self.toExpand = []
        self.targets = targets
        self.position = position
        self.path = Path()
        self.agentNode = agentNode
        self.mapChar = mapChar
        self.objNode = None
        self.bid = Bid(self,100000,None)
        self.bidList = []
        self.otherRobots = []
        self.readyRobot = []

    def step(self):
        print("Ciao sono un agent", self.unique_id)

    def computeNearTargetPath(self):
        t = threading.Thread(target=self.constructTree())
        t.start()

        self.computeBid()
        self.broadCastBid()

    def broadCastBid(self):
        for i in self.otherRobots:
            #print("BIDDER : ", self.bid.bidder, " BID :", self.bid.value," TargetNode", self.bid.targetNode)
            i.receiveBid(self.bid)


    def receiveBid(self, bid):
        self.bidList.append(bid)
        print("I am ROBOT :", self,"/////////////// BID RECEIVED:" , bid.value, "BIDLIST:", self.bidList)
        if len(self.bidList) == len(self.otherRobots):
            print("LUNGHEZZA BIDLIST :", len(self.bidList))
            print("SONO PRONTO A FARE IL WINNER")
            self.computeRoundWinner()


    def computeRoundWinner(self):
        winningBid = 100000000
        winningAgent = None
        for i in self.bidList:
            if i.value < winningBid:
                winningBid = i.value
                winningAgent = i.bidder
        print("WINNING AGENT:", winningAgent)
        self.bidList.clear()
        if self == winningAgent:
            self.updateAllocation()
            x = self.bid.targetNode.xCoord
            y = self.bid.targetNode.yCoord
            self.signTarget(x,y)
            self.sendUpdateMap(x,y)
        self.startNewRound()

    def sendUpdateMap(self, x, y):
        for i in self.otherRobots:
            i.signTarget(x,y)

    def signTarget(self,x , y):
        self.mapChar[x][y] = "t"
        self.targets.remove((x,y))


    def startNewRound(self):
        if len(self.targets) == 0:
            #END OF THE ALGORITHM
            pass
        #i have to update all other robots that i am ready to start a new round
        self.updateRound()


    def updateRound(self):
        for i in self.otherRobots:
            i.ackEndRound(self)


    def ackEndRound(self,robot):
        print(len(self.readyRobot))
        self.readyRobot.append(robot)
        if len(self.readyRobot) == len(self.otherRobots):
            self.readyRobot.clear()
            self.computeNearTargetPath()



    def constructTree(self):
        listPosition = self.getListOfPosition(self.mapChar)
        if self.checkTarget(self.agentNode):
            print("Target Found:", self.agentNode)
            self.objNode = self.agentNode
        else:
            self.toExpand.append(self.agentNode)
            self.setHeuristic(self.agentNode)
            self.expand(self.agentNode, listPosition, self.mapChar)
            self.path = self.constructPath(self.objNode, self.path)
            self.path.path.reverse()
            #self.path.toString()
            self.toExpand.clear()


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

    def computeBid(self):
        pass

    def updateAllocation(self):
        pass



