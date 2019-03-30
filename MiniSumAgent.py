from Agent import Agent
from Bid import Bid


class MiniSumAgent(Agent):
    def __init__(self,nRobots,position,targets, agentNode, mapChar):
        super().__init__(nRobots,position,targets, agentNode, mapChar)
        self.newRPC = len(self.path.path)
        self.oldRPC = 0

        #NON VA QUESTA CAZZO DI COSA
    def computeBid(self):
        print("COMPUTING THE BID")
        value = self.newRPC - self.oldRPC
        target = self.path.path[-1]
        self.bid = Bid(self,value,target)
        self.oldRPC = self.newRPC
        print("BID COMPUTAZIOOO////////////////////////////////////")
        self.bid.toString()

    def updateAllocation(self):
        self.agentNode = self.path.path[-1]


