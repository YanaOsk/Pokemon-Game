"""
@author AchiyaZigi
OOP - Ex4
Very simple GUI example for python client to communicates with the server and "play the game!"
"""
import math
from types import SimpleNamespace
from client import Client
import json
from pygame import gfxdraw
import pygame
from pygame import *
from GraphAlgo import GraphAlgo

# init pygame
WIDTH, HEIGHT = 1080, 720

# default port
PORT = 6666
# server host (default localhost 127.0.0.1)
HOST = '127.0.0.1'
pygame.init()

screen = display.set_mode((WIDTH, HEIGHT), depth=32, flags=RESIZABLE)
clock = pygame.time.Clock()
pygame.font.init()

client = Client()
client.start_connection(HOST, PORT)

pokemons = client.get_pokemons()
pokemons_obj = json.loads(pokemons, object_hook=lambda d: SimpleNamespace(**d))

print(pokemons)

graph_json = client.get_graph()

FONT = pygame.font.SysFont('Arial', 20, bold=True)
# load the json string into SimpleNamespace Object

graph = json.loads(graph_json)
graph_Algo = GraphAlgo()
graph_Algo.load_from_dict(graph)
start = graph_Algo.centerPoint().id
print("graph_Algo = ",graph_Algo)



for n in graph_Algo.get_graph().vertices.values():
    x, y= n.pos
    n.pos = (float(x), float(y))


def min_x():
    min_x = 99999999999
    for i in graph_Algo.get_graph().get_all_v().values():

        print("min_x",min_x)
        print("i.pos[0]", i.pos[0])
        if i.pos[0] < min_x:
            min_x = i.pos[0]
    return min_x


def min_y():
    min_y = 99999999999
    for i in graph_Algo.get_graph().get_all_v().values():
        if i.pos[1] < min_y:
            min_y = i.pos[1]
    return min_y


def max_x():
    max_x = 0
    for i in graph_Algo.get_graph().get_all_v().values():
        if i.pos[0] > max_x:
            max_x = i.pos[0]
    return max_x


def max_y():
    max_y = 0
    for i in graph_Algo.get_graph().get_all_v().values():
        if i.pos[1] > max_y:
            max_y = i.pos[1]
    return max_y
 # get data proportions
min_x = min_x()
min_y = min_y()
max_x = max_x()
max_y = max_y()




def scale(data, min_screen, max_screen, min_data, max_data):
    """
    get the scaled data with proportions min_data, max_data
    relative to min and max screen dimentions
    """
    return ((data - min_data) / (max_data-min_data)) * (max_screen - min_screen) + min_screen


# decorate scale with the correct values

def my_scale(data, x=False, y=False):
    if x:
        return scale(data, 50, screen.get_width() - 50, min_x, max_x)
    if y:
        return scale(data, 50, screen.get_height()-50, min_y, max_y)


radius = 15


dict3 = json.loads(client.get_info())

numOfAgent = dict3['GameServer']['agents']

for i in range(numOfAgent):
    c = "{\"id\":" + str(start+i) + "}"
    client.add_agent(c)


# this commnad starts the server - the game is running now
client.start()

"""
The code below should be improved significantly:
The GUI and the "algo" are mixed - refactoring using MVC design pattern is required.
"""
# print(type(client.get_agents()))
# print(type(client.get_graph()))

# print("zur1: ",type(zur1))
# print(zur1)

while client.is_running() == 'true':
    pokemons = json.loads(client.get_pokemons(),object_hook=lambda d: SimpleNamespace(**d)).Pokemons
    pokemons = [p.Pokemon for p in pokemons]

    for p in pokemons:
        x, y, _ = p.pos.split(',')
        p.pos = SimpleNamespace(x=my_scale(float(x), x=True), y=my_scale(float(y), y=True))
    agents = json.loads(client.get_agents(),object_hook=lambda d: SimpleNamespace(**d)).Agents
    agents = [agent.Agent for agent in agents]
    for a in agents:
        x, y,_ = a.pos.split(',')
        # print("x = ",x)
        # print("y = ", y)
        a.pos = SimpleNamespace(x=my_scale(float(x), x=True), y=my_scale(float(y), y=True))
    # check events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)

    # refresh surface
    screen.fill(Color(0, 0, 0))

    # draw nodes
    for n in graph_Algo.get_graph().vertices.values():
        x = my_scale(n.pos[0], x=True)
        y = my_scale(n.pos[1], y=True)

        # its just to get a nice antialiased circle
        gfxdraw.filled_circle(screen, int(x), int(y),
                              radius, Color(64, 80, 174))
        gfxdraw.aacircle(screen, int(x), int(y),
                         radius, Color(255, 255, 255))

        # draw the node id
        id_srf = FONT.render(str(n.id), True, Color(255, 255, 255))
        rect = id_srf.get_rect(center=(x, y))
        screen.blit(id_srf, rect)

    # draw edges
    for v in graph_Algo.get_graph().vertices:
        for e in graph_Algo.get_graph().all_out_edges_of_node(v):
            # find the edge nodes
            src = graph_Algo.get_graph().vertices[v]
            dest = graph_Algo.get_graph().vertices[e]

            # scaled positions
            src_x = my_scale(src.pos[0], x=True)
            src_y = my_scale(src.pos[1], y=True)
            dest_x = my_scale(dest.pos[0], x=True)
            dest_y = my_scale(dest.pos[1], y=True)

            # draw the line
            pygame.draw.line(screen, Color(61, 72, 126),
                             (src_x, src_y), (dest_x, dest_y))

    # draw agents
    for agent in agents:
        pygame.draw.circle(screen, Color(122, 61, 23),
                           (int(agent.pos.x), int(agent.pos.y)), 10)
    # draw pokemons (note: should differ (GUI wise) between the up and the down pokemons (currently they are marked in the same way).
    for p in pokemons:
        pygame.draw.circle(screen, Color(0, 255, 255), (int(p.pos.x), int(p.pos.y)), 10)

    # update screen changes
    display.update()

    # refresh rate
    clock.tick(60)

    # choose next edge
    for agent in agents:
        if agent.dest == -1:
            # pokemon = None
            # cost = math.inf
            # for p in pokemons:
            #     if p.flag != 1:
            #         if pokemon == None:
            #             pokemon = p
            #             cost = cost(p ,agent )
            #
            #         if cost(p,agent) < cost:
            #             pokemon = p
            #             cost = cost(p, agent)
            # insert p to agent
            # then flag p are inserted

            next_node = (agent.src - 1) % len(graph_Algo.get_graph().vertices.values())
            client.choose_next_edge('{"agent_id":'+str(agent.id)+', "next_node_id":'+str(next_node)+'}')
            ttl = client.time_to_end()
            print(ttl, client.get_info())

    client.move()

def cost(p, a):
    cost = -1
    x, y = line(p)
    if p.type == -1:
        if x < y:
            b, c = graph_algo.shortest_path(a.src, y)
            cost = (b + graph_algo.get_graph().all_out_edges_of_node(y).get(x)) / p.value

        if y < x:
            b, c = graph_algo.shortest_path(a.src, x)
            cost = (b + graph_algo.get_graph().all_out_edges_of_node(x).get(y)) / p.value
    if p.type == 1:
        if x < y:
            b, c = graph_algo.shortest_path(a.src, x)
            cost = (b + graph_algo.get_graph().all_out_edges_of_node(x).get(y)) / p.value
        if y < x:
            b, c = graph_algo.shortest_path(a.src, y)
            cost = (b + graph_algo.get_graph().all_out_edges_of_node(y).get(x)) / p.value
    return cost

def line(pokemon):
    for e in graph.Edges:
        src1 = None
        dest1 = None
        for n in graph.Nodes:
            if n.id == e.src:
                src1 = n
            if n.id == e.dest:
                dest1 = n
        m = (src1.pos.y - dest1.pos.y) / (src1.pos.x - dest1.pos.x)
        if dest1.pos.y == m * (dest1.pos.x - pokemon.pos.x) + pokemon.pos.y:
            return src1, dest1
    return -1






# game over:

