from Agent import *
from MapHandler import *
from Node import *
from Tree import *
from Path import *

agentList = []

def createAgents(robPos,tarPos,mapChar):
    for i in range(len(robPos)):
        agentList.append(Agent(robPos[i],tarPos))
        agentNode = Node(father=None, xCoord=robPos[i][0], yCoord=robPos[i][1],value="R")
        objNode =  agentList[i].constructTree(mapChar,agentNode)
        agentList[i].path = agentList[i].constructPath(objNode,Path())
        agentList[i].path.path.reverse()
        print("AGENT " , i ,":")
        agentList[i].path.toString()

def startRouting(path):
    mapHandler = MapHandler(path)
    mapHandler.readMap()
    mapChar = mapHandler.map
    robotPos = mapHandler.robotPos
    targetPos = mapHandler.targetPos

    createAgents(robotPos,targetPos,mapChar)



startRouting("Map.txt")
