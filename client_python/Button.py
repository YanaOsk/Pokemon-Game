import pygame
class Button:
    def __init__(self, rect: pygame.Rect, color, text, flags, func=None):
        self.rect = rect
        self.color = color
        self.text = text
        self.func = func

        self.is_clicked = False

    def press(self):
        self.is_clicked = not self.is_clicked