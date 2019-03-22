from MapHandler import *

def startRouting(path):
    mapHandler = MapHandler(path)
    mapHandler.readMap()
    

startRouting("Map.txt")