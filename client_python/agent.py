from filecmp import cmp

class agent1:

    def __init__(self,id : int,value : float,src : int,dest : int,speed : float,pos : tuple):
        self.id = id
        self.value = value
        self.src = src
        self.dest = dest
        self.speed = speed
        self.pos = pos
        self.show_pos = pos
        self.next_node = src
        self.path = []
        self.curent_path = 0
        self.tag = -1

    def __str__(self):
        return f"{self.id},{self.value},{self.src},{self.dest},{self.speed},{self.pos}"

    def __repr__(self):
        return f"{self.id},{self.value},{self.src},{self.dest},{self.speed},{self.pos}"
