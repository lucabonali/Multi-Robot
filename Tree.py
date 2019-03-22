class Tree():
    def __init__(self, node):
        self.root = node
        self.children = []

    def addChildren(self, node):
        self.children.append(node)
