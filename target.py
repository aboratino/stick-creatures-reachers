# Stick Creatures - Reachers
# defines a target
#   ~ Anthony Boratino 2013-2019

import pygame.gfxdraw


class Target:
    def __init__(self, screen, x, y):
        self.screen = screen
        self.x = x
        self.y = y
        self.size = 20
        self.color = (200, 100, 10)

    def update(self):
        if self.x < 1024:
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
