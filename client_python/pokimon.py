
class pokimon:
    def __init__(self,value : int,type : int,pos : tuple):
        self.value = value
        self.type = type
        self.pos = pos
        self.tag = -1







def load_from_dict(self, dict: dict) -> bool:
    flag = False
    try:
        for k in dict['Pokemon']:
            n = (k['pos'].split(","))
            pokimon = pokimon(k['value'],k['type'], (float(n[0]), float(n[1])))
            self.graph.add_node(node_id=node.id, pos=node.pos)
        flag = True
    except IOError as e:
        print(e)
    return True