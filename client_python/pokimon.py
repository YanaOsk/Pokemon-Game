from filecmp import cmp

class pokimon:

    def __init__(self,value : float,type : int,pos : tuple):
        self.value = value
        self.type = type
        self.pos = pos
        self.tag = -1
        self.show_pos = pos

    def __str__(self):
        return f"{self.value},{self.type},{self.pos},{self.tag}"

    def __repr__(self):
        return f"{self.value},{self.type},{self.pos},{self.tag}"

