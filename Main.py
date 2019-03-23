from MapHandler import *
from Node import *
from Tree import *
from Path import *

target = "T"
wall = "#"
toExpand = []


def getListOfPosition(mapChar):
    list = []
    for i in range(len(mapChar)):
        for j in range(len(mapChar[i])):
            list.append((i, j))
    return list


def constructTree(mapChar, tree):
    if checkTarget(tree.root):
        print("Target Found:", tree.root)
        return tree
    else:
        tree.addChildren(tree.root)
        toExpand.append(tree.root)
        listPosition = getListOfPosition(mapChar)
        sol = expand(tree, tree.root, listPosition, mapChar)
        return sol

def available(listPosition, coord):
    for i in range(len(listPosition)):
        if listPosition[i] == coord:
            listPosition.remove(coord)
            return True
    return False


def expand(tree, node, listPosition, mapChar):
    toExpand.remove(node)
    for i in range(len(node.adjacents)):
        xCoord = node.adjacents[i][0]
        yCoord = node.adjacents[i][1]
        if available(listPosition,(xCoord,yCoord)):
            try:
                value = mapChar[xCoord][yCoord]
                if not value == wall:
                    child = Node(father=node, xCoord=xCoord, yCoord=yCoord, value=value)
                    node.addChildren(child)
                    tree.children.append(child)
                    toExpand.append(child)
                    #print("I am node:", node.value, node.xCoord, node.yCoord, "Children added :", child.xCoord, child.yCoord, child.value)
            except:
                pass
    for i in range(len(node.children)):
        if checkTarget(node.children[i]):
            print("Solution Found")
            toExpand.clear()
            return node.children[i]
    if not len(toExpand) == 0:
        return expand(tree, toExpand[0], listPosition, mapChar)


def checkTarget(node):
    if node.value == target:
        return True
    return False


def constructPath(node, path):
    if node == None:
        return path
    path.addNode(node)
    return constructPath(node.father,path)



def startRouting(path):
    mapHandler = MapHandler(path)
    mapHandler.readMap()
    mapChar = mapHandler.map
    start = (1, 2)

    mapChar[1][2] = "S"
    mapChar[7][8] = target

    treeRoot = Node(father=None, xCoord=start[0], yCoord=start[1], value=mapChar[start[0]][start[1]])
    tree = Tree(treeRoot)
    targetLeaf = constructTree(mapChar, tree)

    path = constructPath(targetLeaf, Path())
    path.path.reverse()
    path.toString()


startRouting("Map.txt")
