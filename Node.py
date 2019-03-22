class Node():
    def __init__(self,xCoord,yCoord,value):
        self.xCoord = xCoord
        self.yCoord = yCoord
        self.value = value
        self.adjacents = self.initializeAdjList()

    def initializeAdjList(self):
        list = []
        list.append((self.xCoord - 1, self.yCoord - 1))
        list.append((self.xCoord - 1, self.yCoord ))
        list.append((self.xCoord - 1, self.yCoord + 1))
        list.append((self.xCoord , self.yCoord + 1))
        list.append((self.xCoord + 1, self.yCoord + 1))
        list.append((self.xCoord + 1, self.yCoord ))
        list.append((self.xCoord + 1, self.yCoord - 1))
        list.append((self.xCoord , self.yCoord - 1))
        return list