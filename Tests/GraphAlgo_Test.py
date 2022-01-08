import math
from unittest import TestCase

import client_python
from client_python.GraphAlgo import GraphAlgo
from client_python.DiGraph import DiGraph
from client_python.NodeData import Node


class TestGraphAlgo(TestCase):
    graphAlgo = GraphAlgo()


    def making_a_graph_VN(self):
        graph = DiGraph()
        pos = [0, 0, 0]
        for i in range(10):
            graph.add_node(node_id=i, pos=pos)
        graph.add_edge(0, 2, 1)
        graph.add_edge(2, 3, 1)
        graph.add_edge(4, 2, 1.5)
        graph.add_edge(3, 1, 1.8)
        graph.add_edge(5, 4, 3.2)
        graph.add_edge(5, 6, 4.5)
        graph.add_edge(6, 4, 6.7)
        graph.add_edge(7, 6, 7.1)
        graph.add_edge(8, 9, 2.1)
        graph.add_edge(9, 7, 6.8)
        graph.add_edge(3, 4, 6)

        return graph

    def MakingGraph_onlyNodes(self):
        graph = DiGraph()
        pos = [0, 0, 0]
        for i in range(9):
            graph.add_node(i, pos)
        return graph

    def makimgAnEmptyGraph(self):
        graph = DiGraph()
        return graph

    def graph_for_center(self):
        graph_center = DiGraph()
        pos = [0, 0, 0]
        for i in range(4):
            graph_center.add_node(i, pos)
        graph_center.add_edge(0, 1, 0.5)
        graph_center.add_edge(1, 2, 0.1)
        graph_center.add_edge(3, 1, 0.03)
        graph_center.add_edge(2, 0, 0.9)
        graph_center.add_edge(3, 0, 0.01)
        graph_center.add_edge(3, 2, 0.05)
        graph_center.add_edge(2, 1, 9)
        graph_center.add_edge(1, 0, 10)
        return graph_center

    def test_get_graph(self):

        self.graphAlgo.__init__(self.making_a_graph_VN())
        graph = self.making_a_graph_VN()
        self.assertEqual(graph.v_size(), self.graphAlgo.get_graph().v_size())
        self.assertEqual(graph.e_size(), self.graphAlgo.get_graph().e_size())
        self.assertEqual(graph.get_mc(), self.graphAlgo.get_graph().get_mc())
        for i in range(self.graphAlgo.get_graph().v_size()):
            self.assertEqual(graph.get_all_v().get(i).id, self.graphAlgo.get_graph().get_all_v().get(i).id)
            self.assertEqual(graph.get_all_v().get(i).weight, self.graphAlgo.get_graph().get_all_v().get(i).weight)
            self.assertEqual(graph.get_all_v().get(i).pos, self.graphAlgo.get_graph().get_all_v().get(i).pos)
            self.assertEqual(graph.get_all_v().get(i).tag, self.graphAlgo.get_graph().get_all_v().get(i).tag)

    # def test_load_from_json(self):
    #     self.graphAlgo.__init__(self.making_a_graph_VN())
    #
    #     ##print(self.graphAlgo)
    #
    #     graph = GraphAlgo()
    #     graph.save_to_json("../data/graph_VN.json")
    #     graph.load_from_json("graph_VN.json")
    #     ##print(graph)
    #     # self.assertEqual(graph.get_graph(),self.graphAlgo.get_graph()) ##I think the problem is in json file
    #     graph2 = GraphAlgo()
    #     graph2.load_from_json("../data/A1.json")
    #     self.assertNotEqual(graph2.get_graph(), self.graphAlgo.get_graph())

    # def test_save_to_json(self):
    #
    #     self.graphAlgo.__init__(self.making_a_graph_VN())
    #     test = self.graphAlgo
    #     self.graphAlgo.save_to_json("../data/graph_VN.json")
    #     self.graphAlgo.load_from_json("../data/graph_VN.json")
    #     self.assertEqual(test, self.graphAlgo)

    def test_shortest_path(self):
            self.graphAlgo.__init__(self.making_a_graph_VN())
            self.assertEqual(1, self.graphAlgo.shortest_path(0, 2)[0])
            self.assertEqual(20.599999999999998, self.graphAlgo.shortest_path(9, 4)[0])
            self.assertEqual(2.8, self.graphAlgo.shortest_path(2, 1)[0])
            self.assertEqual(4.5, self.graphAlgo.shortest_path(5, 6)[0])
            self.assertEqual(4.5, self.graphAlgo.shortest_path(5, 6)[0])
            self.assertEqual(20.599999999999998, self.graphAlgo.shortest_path(9, 4)[0])



    def test_tsp(self):
        self.graphAlgo.__init__(self.making_a_graph_VN())
        self.assertEqual((None, math.inf), self.graphAlgo.TSP([1, 2, 3]))
        self.assertEqual(([2, 3, 4], 8.5), self.graphAlgo.TSP([2, 3, 4]))

    def test_center_point(self):
        self.graphAlgo.__init__(self.graph_for_center())
        self.assertEqual(str(3), str(self.graphAlgo.centerPoint()))
        self.assertNotEqual(0, self.graphAlgo.centerPoint())
        self.assertNotEqual(1, self.graphAlgo.centerPoint())
        self.assertNotEqual(2, self.graphAlgo.centerPoint())
