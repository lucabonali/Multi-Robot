

class MapHandler():
    def __init__(self, path):
        self.path = path

    def readMap(self):
        f = open(self.path, "r")
        height = sum(1 for line in open(self.path))
        self.map = [None] * height
        for i in range(height):
            self.map[i] = list(f.readline().rstrip())


