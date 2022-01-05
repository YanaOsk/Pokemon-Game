# from student_code import *
import pygame
####################### C L A S S    B U T T O N #########################
from pygame import display, RESIZABLE
from pygame import *
from pygame.color import Color

WIDTH, HEIGHT = 300, 300
pygame.init()
screen = display.set_mode((WIDTH, HEIGHT), depth=32, flags=RESIZABLE)
screen.fill((200, 200, 0))
# pygame.draw.rect(screen, button.color, button.rect)
font = pygame.font.SysFont("Arial", 20)
clock = pygame.time.Clock()
pygame.font.init()



class Button:
    def __init__(self, rect: pygame.Rect, color, text, func=None):
        self.rect = rect
        self.color = color
        self.text = text
        self.func = func
        self.is_clicked = False
        self.surface= pygame.Surface((50,50))

    def press(self):
        self.is_clicked = not self.is_clicked


button = Button(pygame.Rect((70, 20), (100, 100)), (200, 200, 0), "Algo")
##########################################################################

result = []
def on_clicked(button:Button):
    global result
    result=button.func()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)
    # if event.type == pygame.MOUSEBUTTONDOWN:
    #     # if button.rect.collidepoint(event.pos):
    #     #     button.func = display
    # # refresh surface
    screen.blit(button.surface,(10,10))
    (10,10)
    pygame.display.update()

    # refresh rate


