from MapHandler import *
from Node import *
from Tree import *

def constructNodesMap(map):
    for i in range(len(map)):
        for j in range(len(map[i])):
            v = map[i][j]
            map[i][j] = Node(i,j,v)
    return map


def constructTree(start, target, map):
    tree = Tree(map[start[0]][start[1]])
    if()



def startRouting(path):
    mapHandler = MapHandler(path)
    mapHandler.readMap()
    map = constructNodesMap(mapHandler.map)
    start = (1,2)
    target = (7,8)
    map[1][2] = Node(1,2,"S")
    map[7][8] = Node(7,8,"T")

    constructTree(start,target,map)


startRouting("Map.txt")