class Node():
    def __init__(self,xCoord,yCoord,value):
        self.xCoord = xCoord
        self.yCoord = yCoord
        self.value = value
        self.adjacents = self.initializeAdjList()

    def initializeAdjList(self):
        list = []
        list[0] = (self.xCoord - 1, self.yCoord - 1)
        list[1] = (self.xCoord - 1, self.yCoord )
        list[2] = (self.xCoord - 1, self.yCoord + 1)
        list[3] = (self.xCoord , self.yCoord + 1)
        list[4] = (self.xCoord + 1, self.yCoord + 1)
        list[5] = (self.xCoord + 1, self.yCoord )
        list[6] = (self.xCoord + 1, self.yCoord - 1)
        list[7] = (self.xCoord , self.yCoord - 1)
        return list