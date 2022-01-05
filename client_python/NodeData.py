from filecmp import cmp



class Node:
    def __init__(self, node_id : int = 0 , pos: tuple = (), tag=-1, weight: int = 0):
        self.id = node_id
        self.pos = pos
        self.tag = tag
        self.weight = weight
        self.inEdges = {}
        self.outEdges = {}



    def __lt__(self, compare_node):
        return self.weight < compare_node.weight


    def __str__(self):
        return f"{self.id}"

    def __repr__(self):
        return f"{self.id}"
