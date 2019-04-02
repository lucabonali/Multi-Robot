from RoutingAgent import RoutingAgent
from Bid import Bid


class MiniSumRoutingAgent(RoutingAgent):
    def __init__(self,unique_id, model,nRobots,position,targets, agentNode, mapChar):
        super().__init__(unique_id, model,nRobots,position,targets, agentNode, mapChar)
        self.newRPC = 0
        self.oldRPC = 0


    def computeBid(self):
        self.newRPC = len(self.path.path)
        value = self.newRPC - self.oldRPC
        target = self.path.path[-1]
        self.bid.value = value
        self.bid.targetNode = target
        self.oldRPC = self.newRPC


    def updateAllocation(self):
        self.agentNode = self.path.path[-1]


