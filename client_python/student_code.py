"""
@author AchiyaZigi
OOP - Ex4
Very simple GUI example for python client to communicates with the server and "play the game!"
"""
import math
from types import SimpleNamespace
from fontTools.misc.bezierTools import epsilon
from client import Client
import json
from pygame import gfxdraw
import pygame
from pygame import *
from GraphAlgo import GraphAlgo
from pokimon import pokimon
from agent import agent1


####################### C L A S S    B U T T O N #########################
class Button:
    def __init__(self, rect: pygame.Rect, color, text, func=None):
        self.rect = rect
        self.color = color
        self.text = text
        self.func = func

        self.is_clicked = False

    def press(self):
        self.is_clicked = not self.is_clicked


button = Button(pygame.Rect((900, 650), (150, 50)), (250, 0, 0), "Stop the game")
##########################################################################




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
pok_image = pygame.image.load('pokpok.png')


counter, text = 30, '30'.rjust(3)
pygame.time.set_timer(pygame.USEREVENT, 1000)
font = pygame.font.SysFont('Consolas', 30)


client = Client()
client.start_connection(HOST, PORT)

"""
pokemons_obj = json.loads(pokemons, object_hook=lambda d: SimpleNamespace(**d))
"""

graph_json = client.get_graph()

FONT = pygame.font.SysFont('comicsansms', 20, bold=True)
# load the json string into SimpleNamespace Object

graph = json.loads(graph_json)
graph_Algo = GraphAlgo()
graph_Algo.load_from_dict(graph)
start = graph_Algo.centerPoint().id

print("graph_Algo = ", graph_Algo)

for n in graph_Algo.get_graph().vertices.values():
    x, y = n.pos
    n.pos = (float(x), float(y))


def min_x():
    min_x = 99999999999
    for i in graph_Algo.get_graph().get_all_v().values():
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
    return ((data - min_data) / (max_data - min_data)) * (max_screen - min_screen) + min_screen


# decorate scale with the correct values

def my_scale(data, x=False, y=False):
    if x:
        return scale(data, 50, screen.get_width() - 50, min_x, max_x)
    if y:
        return scale(data, 50, screen.get_height() - 50, min_y, max_y)


radius = 15

dict3 = json.loads(client.get_info())

numOfAgent = dict3['GameServer']['agents']

for i in range(numOfAgent):
    c = "{\"id\":" + str(start + i) + "}"
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
    pokemons_List = []
    pokemons = client.get_pokemons()
    pokemons2 = json.loads(pokemons)


    def load_from_pokemon_dict(dict: dict) -> bool:
        flag = False
        for i in range(len(dict['Pokemons'])):
            for k in dict['Pokemons']:
                n = (k['Pokemon']['pos'].split(","))
                pok = pokimon(k['Pokemon']['value'], k['Pokemon']['type'], (float(n[0]), float(n[1])),i)
                flag = True
            pokemons_List.append(pok)
        return flag


    load_from_pokemon_dict(pokemons2)

    for p in pokemons_List:
        x, y = p.pos
        p.show_pos = (my_scale(float(x), x=True), my_scale(float(y), y=True))

    agents_list = []
    agents = client.get_agents()
    agents2 = json.loads(agents)


    def load_from_agent_dict(dict: dict) -> bool:
        flag = False
        for k in dict['Agents']:
            n = (k['Agent']['pos'].split(","))
            age = agent1(k['Agent']['id'], k['Agent']['value'], k['Agent']['src'], k['Agent']['dest'],
                         k['Agent']['speed'], (float(n[0]), float(n[1])))

            agents_list.append(age)
            flag = True
        return flag


    load_from_agent_dict(agents2)

    for a in agents_list:
        x, y = a.pos
        a.show_pos = (my_scale(float(x), x=True), my_scale(float(y), y=True))

    # check events
    for event in pygame.event.get():
        if event.type == pygame.USEREVENT:
            counter -= 1
            text = str(counter).rjust(3) if counter > 0 else '  Game Over'
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)
        if event.type == pygame.MOUSEBUTTONDOWN:
            if button.rect.collidepoint(event.pos):
                button.func=client.stop_connection()
    # refresh surface
    screen.fill(Color(243, 233, 0))
    screen.blit(pok_image, (300, 10))
    pygame.draw.rect(screen, button.color, button.rect)
    button_text=FONT.render(button.text,True,(0,0,0))
    text_to_end = FONT.render('Time to end :', True, (0, 0, 0))
    screen.blit(button_text,(button.rect.x+6,button.rect.y+6))
    screen.blit(font.render(text, True, (0, 0, 0)), (150, 40))
    screen.blit(text_to_end,(30,40))

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
    for a in agents_list:
        pygame.draw.circle(screen, Color(122, 61, 23), (int(a.show_pos[0]), int(a.show_pos[1])), 10)
    # draw pokemons (note: should differ (GUI wise) between the up and the down pokemons (currently they are marked in the same way).
    for p in pokemons_List:
        pygame.draw.circle(screen, Color(0, 255, 255), (int(p.show_pos[0]), int(p.show_pos[1])), 10)
        id_srf_pok = FONT.render(str(p.id), True, Color(0, 0, 0))
        rect = id_srf_pok.get_rect(center=(int(p.show_pos[0]), int(p.show_pos[1])))
        screen.blit(id_srf_pok, rect)

    # update screen changes
    display.update()

    # refresh rate
    clock.tick(10)



    def line(pokemon):

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
                        if  e < v.id:
                            return v.id, e
                    if pokemon.type == 1:
                        if v.id < e:
                            return v.id, e
                        if e < v.id:
                            return e, v.id
        return -1


    def cost(p, a):
        cost = -1
        x, y = line(p)
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
    # choose next edge
    for agent in agents_list:
        if agent.dest == -1:

            cost1 = 99999999999999
            temp_pokemons = None

            for p in pokemons_List:

                if p.tag == -1:
                    if cost(p,agent) < cost1:
                        cost1 = cost(p,agent)
                        temp_pokemons = p



            if temp_pokemons != None:
                temp_pokemons.tag = 1
                start_e, end_e = line(temp_pokemons)

                boring,path = graph_Algo.shortest_path(agent.src,start_e)
                path.append(end_e)
                a = 1
                agent.next_node = path[a]



                client.choose_next_edge('{"agent_id":'+str(agent.id)+', "next_node_id":'+str(agent.next_node)+'}')
                a += 1

                ttl = client.time_to_end()

    if int(ttl) <30:
        print(client.get_info())

    client.move()