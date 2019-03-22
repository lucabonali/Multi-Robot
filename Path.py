class Path():
    def __init__(self):
        self.path = []
        self.len = 0

    def addNode(self, node):
        self.path.append(node)
        self.len += 1