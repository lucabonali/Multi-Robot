from colorama import Fore

from Agent import Agent
from MapHandler import *
from Node import Node


class Auction():
    def __init__(self):
        self.mapChar = []
        self.robotPos = []
        self.targetPos = []
        self.agentList = []


    def startRoutingAuction(self, path):
        mapHandler = MapHandler(path)
        mapHandler.readMap()
        self.mapChar = mapHandler.map
        self.robotPos = mapHandler.robotPos
        self.targetPos = mapHandler.targetPos
        self.createAgents(self.robotPos, self.targetPos, self.mapChar)
        drawer = self.Drawer(self.agentList)
        drawer.printMap(self.mapChar)

    def createAgents(self,robPos, tarPos, mapChar):
        for i in range(len(robPos)):
            agentNode = Node(father=None, xCoord=robPos[i][0], yCoord=robPos[i][1], value="R")
            self.agentList.append(Agent(robPos[i], tarPos, agentNode, mapChar))
            self.agentList[i].run()






    class Drawer():
        def __init__(self,agentList):
            self.colorList = []
            self.agentList = agentList

        def initializeColorList(self):
            self.colorList.append(Fore.GREEN)
            self.colorList.append(Fore.BLUE)
            self.colorList.append(Fore.RED)
            self.colorList.append(Fore.CYAN)
            self.colorList.append(Fore.LIGHTMAGENTA_EX)

        def colorPaths(self,mapChar):
            self.initializeColorList()
            for i in range(len(self.agentList)):
                for j in range(len(self.agentList[i].path.path) - 1):
                    xCoord = self.agentList[i].path.path[j].xCoord
                    yCoord = self.agentList[i].path.path[j].yCoord
                    mapChar[xCoord][yCoord] = self.colorList[i] + "*" + Fore.WHITE


        def printMap(self,mapChar):
            self.colorPaths(mapChar)
            for i in range(len(mapChar)):
                print("".join(mapChar[i]))