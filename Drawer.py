from colorama import Fore


class Drawer():
    def __init__(self, agentList):
        self.colorList = []
        self.agentList = agentList

    def initializeColorList(self):
        self.colorList.append(Fore.GREEN)
        self.colorList.append(Fore.BLUE)
        self.colorList.append(Fore.RED)
        self.colorList.append(Fore.CYAN)
        self.colorList.append(Fore.LIGHTMAGENTA_EX)

    def colorPaths(self, mapChar):
        self.initializeColorList()
        for i in self.agentList:
            for j in range(len(i.path.path) - 1):
                xCoord = i.path.path[j].xCoord
                yCoord = i.path.path[j].yCoord
                mapChar[xCoord][yCoord] = self.colorList[i] + "*" + Fore.WHITE

    def printMap(self, mapChar):
        self.colorPaths(mapChar)
        for i in mapChar:
            print("".join(i))

#to draw the map, needs the list of agents and the updated mapchar
'''
drawer = Drawer(self.schedule.agents)
drawer.printMap(self.mapChar)
'''