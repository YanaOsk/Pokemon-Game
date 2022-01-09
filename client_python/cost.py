import math
from fontTools.misc.bezierTools import epsilon
from client_python.client import Client
import json
from pygame import gfxdraw
import pygame
from pygame import *
from client_python.GraphAlgo import GraphAlgo
from client_python.pokimon import pokimon
from client_python.agent import agent1
from client_python import *

class cost_line:

    def cost(p, a,graph_Algo):
        cost = -1
        x, y = cost_line.line(p,graph_Algo)
        if p.type == -1:
            if x < y:
                b, c = graph_Algo.shortest_path(a.src, y)
                cost = (b + graph_Algo.get_graph().all_out_edges_of_node(y).get(x)) / p.value

            if y < x:
                b, c = graph_Algo.shortest_path(a.src, x)
                cost = (b + graph_Algo.get_graph().all_out_edges_of_node(x).get(y)) / p.value
        if p.type == 1:
            if x < y:
                b, c = graph_Algo.shortest_path(a.src, x)
                cost = (b + graph_Algo.get_graph().all_out_edges_of_node(x).get(y)) / p.value
            if y < x:
                b, c = graph_Algo.shortest_path(a.src, y)
                cost = (b + graph_Algo.get_graph().all_out_edges_of_node(y).get(x)) / p.value
        return cost

    def line(pokemon,graph_Algo):

        """
        :param pokemon:
        :return:
        """
        flag = True
        for v in graph_Algo.get_graph().vertices.values():  ## here we get the node object
            for e in graph_Algo.get_graph().all_out_edges_of_node(v.id):  ## here we get
                y2 = v.pos[1]
                y1 = graph_Algo.get_graph().get_all_v()[e].pos[1]
                x2 = v.pos[0]
                x1 = graph_Algo.get_graph().get_all_v()[e].pos[0]
                y3 = pokemon.pos[1]
                x3 = pokemon.pos[0]
                a = (y2 - y1) / (x2 - x1)
                b = y1 - a * x1
                if abs(y3 - (a * x3 + b)) < epsilon:
                    if pokemon.type == -1:
                        if v.id < e:
                            return e, v.id
                        if e < v.id:
                            return v.id, e
                    if pokemon.type == 1:
                        if v.id < e:
                            return v.id, e
                        if e < v.id:
                            return e, v.id
        return -1