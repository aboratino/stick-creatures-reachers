# Stick Creatures - Reachers
# defines creature and segment class
#   ~ Anthony Boratino 2013-2019

import pygame
import pygame.gfxdraw
from random import randrange, random
import math


WHITE = (255, 255, 255)     # Some colors
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)

START_Y = 700               # root location of all creatures
START_X = 512

CHANCE = 5                  # One in 'CHANCE' chance of mutation.
N_SEG = 35                  # number of segments per creature
MUTATE_MULTIPLIER = 80      # Used to magnify the value of mutation


# class Creature
class Segment:
    def __init__(self, screen):
        self.screen = screen            # screen to draw on
        self.length = 18                # segment length
        self.bx = 0                     # begin x
        self.by = 0                     # begin y
        self.ex = 0                     # end x
        self.ey = 0                     # end y
        self.grotation = 0              # segments genenetic start rotation
        self.rotation = 0               # segments current rotation
        self.is_first = False
        self.is_last = False

    def draw(self):

        # draw lines to represent segments
        pygame.gfxdraw.line(self.screen, int(self.bx), int(self.by), int(self.ex), int(self.ey), WHITE)

        if not self.is_first and not self.is_last:
            pygame.gfxdraw.filled_circle(self.screen, int(self.bx), int(self.by), 3, BLUE)

        # if first point
        if self.is_first:
            pygame.gfxdraw.filled_circle(self.screen, int(self.bx), int(self.by), 6, GREEN)

        # if last point
        if self.is_last:
            pygame.gfxdraw.filled_circle(self.screen, int(self.ex), int(self.ey), 4, GREEN)
            pygame.gfxdraw.filled_circle(self.screen, int(self.bx), int(self.by), 3, BLUE)
# End class Creature


# class Creature
class Creature:
    def __init__(self, cid, screen):
        self.cid = cid                  # creature id
        self.screen = screen
        self.n_segments = N_SEG
        self.limb = []

        # create segments, initialize starting rotations of segments and
        # initialize rotation rates of segments.
        for i in range(self.n_segments):
            self.limb.append(Segment(self.screen))
            self.limb[i].grotation = self.limb[i].rotation = randrange(0, 360)

        self.limb[0].is_first = True
        self.limb[-1].is_last = True

    def new_ex(self, i):
        return self.limb[i].length * math.sin(self.limb[i].rotation * (math.pi / 180.0))

    def new_ey(self, i):
        return self.limb[i].length * math.cos(self.limb[i].rotation * (math.pi / 180.0))

    def calc_endpoint(self, i):
        self.limb[i].ex = self.limb[i].bx + self.new_ex(i)
        self.limb[i].ey = self.limb[i].by + self.new_ey(i)

    # update location of segments
    def update(self):
        self.limb[0].bx = START_X
        self.limb[0].by = START_Y
        self.calc_endpoint(0)

        for i in range(1, self.n_segments):
            self.limb[i].bx = self.limb[i - 1].ex
            self.limb[i].by = self.limb[i - 1].ey
            self.calc_endpoint(i)

    @staticmethod
    def mutate():
        if randrange(CHANCE) == 1:
            return (random() - 0.5) * MUTATE_MULTIPLIER
        else:
            return 0

    # draw all the segments
    def draw(self):
        for i in range(self.n_segments):
            self.limb[i].draw()

    # return location of head
    def get_loc(self):
        return self.limb[-1].ex, self.limb[-1].ey

    # breed, for each segment blend and mutate with winner's segments
    def breedwith(self, best):
        for i in range(self.n_segments):
            self.limb[i].rotation = ((self.limb[i].rotation + best.limb[i].grotation) / 2) + self.mutate()
            self.limb[i].grotation = self.limb[i].rotation
# End class Creature

