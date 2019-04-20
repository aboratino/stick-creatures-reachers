# Stick Creatures - Reachers
# defines a target
#   ~ Anthony Boratino 2013-2019

import pygame.gfxdraw

COLOR_TARGET = (200, 100, 10)
SIZE_TARGET = 20


class Target:
    def __init__(self, screen, x, y):
        self.screen = screen
        self.x = x
        self.y = y
        self.size = SIZE_TARGET
        self.color = COLOR_TARGET

    def update(self):
        if self.x < self.screen.get_width():
            self.x += 1
        else:
            self.x = 1

    def draw(self):
        self.update()
        pygame.gfxdraw.filled_circle(self.screen,
                                     int(self.x),
                                     int(self.y),
                                     self.size,
                                     self.color)

    def get_loc(self):
        return self.x, self.y
