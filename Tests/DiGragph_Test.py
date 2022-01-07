from unittest import TestCase
from client_python.NodeData import Node
from client_python.DiGraph import DiGraph


class TestDiGraph(TestCase):
    size = 10

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
        return graph

    def MakingGraph_onlyNodes(self):
        graph = DiGraph()
        pos = [0, 0, 0]
        for i in range(9):
            graph.add_node(i, pos)
        return graph

    def test_v_size(self):
        graph = self.MakingGraph_onlyNodes()
        pos = [0, 0, 0]
        self.assertTrue(graph.v_size() == 9)
        graph.add_node(12, pos)
        graph.add_node(13, pos)
        self.assertTrue(graph.v_size() == 11)

    def test_e_size(self):
        graph = self.making_a_graph_VN()
        self.assertTrue(graph.e_size() == 10)
        graph.add_edge(1, 9, 0.5)
        graph.add_edge(6, 3, 0.3)
        graph.add_edge(2, 5, 0.9)
        self.assertTrue(graph.e_size() == 13)
        graph.remove_edge(1, 9)
        self.assertTrue(graph.e_size() == 12)

    def test_get_all_v(self):
        graph = self.making_a_graph_VN()
        self.assertEqual(10, len(graph.get_all_v()))
        graph.remove_node(1)
        self.assertEqual(9, len(graph.get_all_v()))
        graph.add_node(1)
        self.assertEqual(10, len(graph.get_all_v()))
        for i in range(10):
            graph.remove_node(i)
        self.assertEqual({}, graph.get_all_v())

    def test_all_in_edges_of_node(self):
        graph = DiGraph()
        graph = self.making_a_graph_VN()
        self.assertEqual({}, graph.all_in_edges_of_node(5))
        self.assertEqual({8: 2.1}, graph.all_in_edges_of_node(9))

    def test_all_out_edges_of_node(self):
        graph = self.making_a_graph_VN()
        self.assertEqual(0, len(graph.all_out_edges_of_node(1)))
        self.assertEqual(1, len(graph.all_out_edges_of_node(2)))
        self.assertEqual(2, len(graph.all_out_edges_of_node(5)))
        self.assertEqual(1, len(graph.all_out_edges_of_node(6)))
        graph.remove_edge(5, 4)
        self.assertEqual(1, len(graph.all_out_edges_of_node(5)))

    def test_get_mc(self):
        graph = self.making_a_graph_VN()
        graph.add_node(16)
        self.assertTrue(graph.countMc == 21)

    def test_add_edge(self):
        graph = self.making_a_graph_VN()
        self.assertFalse(graph.add_edge(0, 2, 1))
        self.assertFalse(graph.add_edge(0, 2, 2))
        self.assertFalse(graph.add_edge(2, 3, 1))
        self.assertTrue(graph.add_edge(3, 7, 1))
        self.assertTrue(graph.add_edge(1, 4, 1))

    def test_add_node(self):
        graph = self.MakingGraph_onlyNodes()
        pos = [0, 0, 0]
        self.assertTrue(graph.v_size() == 9)
        graph.add_node(12, pos)
        graph.add_node(13, pos)
        self.assertTrue(graph.v_size() == 11)

    def test_remove_node(self):
        graph = self.MakingGraph_onlyNodes()
        pos = [0, 0, 0]
        self.assertTrue(graph.v_size() == 9)
        graph.add_node(12, pos)
        graph.add_node(13, pos)
        self.assertTrue(graph.v_size() == 11)
        graph.remove_node(12)
        graph.remove_node(13)
        self.assertTrue(graph.v_size() == 9)

    # def test_remove_edge(self):
    #     self.fail()
    #
    # def test_remove_edge(self):
    #     self.fail()
    #
    # def test_as_dict(self):
    #     self.fail()