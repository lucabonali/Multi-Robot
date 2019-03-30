class Bid():
    def __init__(self, bidder, value, targetNode):
        self.value = value
        self.bidder = bidder
        self.targetNode = targetNode

    def toString(self):
        print("BIDDER : ", self.bidder, " BID :", self.value," TargetNode", self.targetNode)