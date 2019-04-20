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
NUM_SEGMENTS = 35           # number of segments per creature
LENGTH_SEG = 18

MUTATE_MULTIPLIER = 80      # Used to magnify the value of mutation

SIZE_JOINT = 3
SIZE_BASE = 5
SIZE_END = 5


class Segment:
    def __init__(self, grot):
        self.bx = 0             # begin x
        self.by = 0             # begin y
        self.ex = 0             # end x
        self.ey = 0             # end y
        self.grot = grot        # segments genetic start rotation
        self.rot = grot         # segments current rotation


class Creature:
    def __init__(self, screen):
        self.screen = screen        # screen to draw on
        self.limb = []              # an array of of limbs

        # append segments with random rotations to limb
        for i in range(NUM_SEGMENTS):
            self.limb.append(Segment(randrange(0, 360)))

        # set base location of the first limb
        self.limb[0].bx = START_X
        self.limb[0].by = START_Y

    # return new x and y for endpoints
    def new_ex(self, i):
        return int(LENGTH_SEG * math.sin(self.limb[i].rot * (math.pi / 180.0)))

    def new_ey(self, i):
        return int(LENGTH_SEG * math.cos(self.limb[i].rot * (math.pi / 180.0)))

    # calculate new endpoints
    def calc_endpoint(self, i):
        self.limb[i].ex = self.limb[i].bx + self.new_ex(i)
        self.limb[i].ey = self.limb[i].by + self.new_ey(i)

    # update location of segments
    def update(self):
        # calculate first segments endpoint
        self.calc_endpoint(0)

        # calculate the rest
        for i in range(1, NUM_SEGMENTS):
            self.limb[i].bx = self.limb[i - 1].ex
            self.limb[i].by = self.limb[i - 1].ey
            self.calc_endpoint(i)

    # One in 'CHANCE' chance to return a mutation value between -0.5 and 0.5
    @staticmethod
    def mutate():
        if randrange(CHANCE) == 1:
            return (random() - 0.5) * MUTATE_MULTIPLIER
        else:
            return 0

    # draw all the segments
    def draw(self):
        for i in range(NUM_SEGMENTS):

            # draw lines to represent segments
            pygame.gfxdraw.line(self.screen,
                                self.limb[i].bx,
                                self.limb[i].by,
                                self.limb[i].ex,
                                self.limb[i].ey,
                                WHITE)

            # if first segment draw a base
            if i == 0:
                pygame.gfxdraw.filled_circle(self.screen,
                                             self.limb[i].bx,
                                             self.limb[i].by,
                                             SIZE_BASE,
                                             GREEN)

            # draw a 'joint' between segments
            if i and i < NUM_SEGMENTS-1:
                pygame.gfxdraw.filled_circle(self.screen,
                                             self.limb[i].bx,
                                             self.limb[i].by,
                                             SIZE_JOINT,
                                             BLUE)

            # if last segment draw the last joint and tip
            if i == NUM_SEGMENTS-1:
                pygame.gfxdraw.filled_circle(self.screen,
                                             self.limb[i].bx,
                                             self.limb[i].by,
                                             SIZE_JOINT,
                                             BLUE)
                pygame.gfxdraw.filled_circle(self.screen,
                                             self.limb[i].ex,
                                             self.limb[i].ey,
                                             SIZE_END,
                                             GREEN)

    # return location of head
    def get_loc(self):
        return self.limb[-1].ex, self.limb[-1].ey

    # breed, for each segment blend and mutate with winner's segments
    def breedwith(self, best):
        for i in range(NUM_SEGMENTS):
            self.limb[i].rot = ((self.limb[i].rot + best.limb[i].grot) / 2) + self.mutate()
            self.limb[i].grot = self.limb[i].rot
# End class Creature
