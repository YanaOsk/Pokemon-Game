import copy

from src.GraphInterface import GraphInterface
from src.NodeData import Node


class DiGraph(GraphInterface):

    def __init__(self):
        self.numOfVertices = 0
        self.numOfEdges = 0
        self.countMc = 0
        self.vertices = {}


    def __copy__(self, other):
         """todo implement me"""

    def v_size(self) -> int:
       return self.numOfVertices

    def e_size(self) -> int:
        return self.numOfEdges

    def get_all_v(self) -> dict:
        """
        zur's implementation
        :return:
        """
        return self.vertices

    def get_edges(self):
        return self.edges

    def all_in_edges_of_node(self, id1: int) -> dict:
        """
        this function is checking, if the given node's id is
        in value of another node's id,
        which means, that they are connected
        if it is , i put the node in another dictionary
        and return the dictionary
        :param id1:
        :return:
        """
        if id1 in self.vertices:
            return self.vertices.get(id1).inEdges
        return None

    def all_out_edges_of_node(self, id1: int) -> dict:
        """
        zur's implementation
        :param id1:
        :return:
        """
        if id1 in self.vertices:
            return self.vertices.get(id1).outEdges
        return None

    def get_mc(self) -> int:
        return self.countMc

    def add_edge(self, id1: int, id2: int, weight: float) -> bool:
        """
        zur's implementation
        :param id1:
        :param id2:
        :param weight:
        :return:
        """
        if id1 in self.vertices and id2 in self.vertices:
            if id2 not in self.vertices.get(id1).outEdges:
                self.vertices.get(id1).outEdges[id2] = weight
                self.vertices.get(id2).inEdges[id1] = weight
                self.numOfEdges += 1
                self.countMc += 1
                return True
            return False


    def add_node(self, node_id: int, pos: tuple = None) -> bool:
        """
        this function is adding the object Node to a dictionary
        if it is not there
        also we are updating the ModeCount and the amount of vertices
        in our graph
        i used the self.vertices.update(...), because i think that
        it is instead of .add
        see here - https://stackoverflow.com/questions/1024847/how-can-i-add-new-keys-to-a-dictionary
        :param node_id:
        :param pos:
        :return:
        """
        if node_id not in self.vertices:
            node = Node(node_id, pos)
            self.vertices[node_id] = node
            self.countMc += 1
            self.numOfVertices += 1
            return True
        return False

    def remove_node(self, node_id: int) -> bool:
        """
        zur's implementation
        :param node_id:
        :return:
        """
        if node_id in self.vertices:
            if self.all_out_edges_of_node(node_id).keys() is not None:
                for i in self.all_out_edges_of_node(node_id).keys():
                    self.vertices.get(i).inEdges.pop(node_id)
                    self.numOfEdges -= 1
            if self.all_in_edges_of_node(node_id).keys() is not None:
                for i in self.all_in_edges_of_node(node_id).keys():
                    self.vertices.get(i).outEdges.pop(node_id)
                    self.numOfEdges -= 1
            self.vertices.pop(node_id)
            self.numOfVertices -= 1
            self.countMc += 1
            return True
        return False

    def remove_edge(self, node_id1: int, node_id2: int) -> bool:
        """
        i am not sure about this implementation
        but i am checking if both of id are in vertices dict
        then i check if given id is contains in a value of another id
        if yes , i remove it
        :param node_id1:
        :param node_id2:
        :return:
        """
        ans = False
        if node_id1 in self.vertices and node_id2 in self.vertices:
            if node_id2 in self.vertices.get(node_id1).outEdges:
                self.vertices.get(node_id1).outEdges.pop(node_id2)
                self.vertices.get(node_id2).inEdges.pop(node_id1)
                self.countMc += 1
                self.numOfEdges -= 1
                ans = True
        return ans

    def as_dict(self):
        try:
            nodes = []
            new_dict = {}
            for n in self.get_all_v().values():
                if len(n.pos) == 0:
                    node = {'id': n.id}
                elif len(n.pos) == 2:
                    node = {'id': n.id, 'pos': f"{n.pos[0]},{n.pos[1]}"}
                else:
                    node = {'id': n.id, 'pos': f"{n.pos[0]},{n.pos[1]},{n.pos[2]}"}
                nodes.append(node)
            new_dict['Nodes'] = nodes
            edges = []
            for k in self.vertices.keys():
                for dest, weight in self.all_in_edges_of_node(k).items():
                    edge = {'src': k, 'dest': dest, 'w': weight}
                    edges.append(edge)
            new_dict['Edges'] = edges
        except IOError as e:
            print(e)
        return new_dict



    def __str__(self):
        return f"{self.vertices},{self.numOfVertices},{self.numOfEdges},{self.countMc}"

    def __repr__(self):
        return f"{self.vertices},{self.numOfVertices},{self.numOfEdges},{self.countMc}"