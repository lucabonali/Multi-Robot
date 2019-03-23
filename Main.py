from MapHandler import *
from Node import *
from Tree import *
from Path import *

target = "T"


def getListOfPosition(mapChar):
    list = []
    for i in range(len(mapChar)):
        for j in range(len(mapChar[i])):
            list.append((i, j))
    return list


def constructTree(mapChar, tree):
    if checkTarget(tree.root):
        return tree
    else:
        listPosition = getListOfPosition(mapChar)
        addChildrenToTree(tree.root, listPosition, mapChar)


def alreadyIn(listPosition, coord):
    for i in range(len(listPosition)):
        if listPosition[i] == coord:
            return True
    return False


def addChildrenToTree(node, listPosition, mapChar):
    for i in range(len(node.adjacents)):
        xCoord = node.adjacents[i][0]
        yCoord = node.adjacents[i][1]
        if not alreadyIn(listPosition, (xCoord, yCoord)):
            listPosition.remove((xCoord, yCoord))
            try:
                value = mapChar[xCoord][yCoord]
                child = Node(father=node, xCoord=xCoord, yCoord=yCoord, value=value)
                node.addChildren(child)
                if not value == target:
                    addChildrenToTree(node.children[i], listPosition, mapChar)
            except:
                pass


def checkTarget(node):
    if node.value == target:
        return True
    return False


def addNodeToPath(path, treeRoot, index):
    path.addNode(treeRoot.children[index])
    addNodeToPath(treeRoot.children[index])


def constructPath(treeRoot):
    path = Path()
    addNodeToPath(path,treeRoot, 0)


def startRouting(path):
    mapHandler = MapHandler(path)
    mapHandler.readMap()
    mapChar = mapHandler.map
    start = (1, 2)
    target = (7, 8)
    mapChar[1][2] = "S"
    mapChar[7][8] = target

    treeRoot = Node(father=None, xCoord=start[0], yCoord=start[1], value=mapChar[start[0]][start[1]])
    tree = Tree(treeRoot)
    constructTree(mapChar, tree)

    constructPath(treeRoot)


startRouting("Map.txt")
