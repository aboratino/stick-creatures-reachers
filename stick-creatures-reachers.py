# ===================================
# Stick Creatures - Reachers
#   Anthony Boratino 2013-2019
#
#   Simulate evolution of 'reacher' stick creatures
#   Each creature consists of an array of segments.
#
#   Explores tentacles that reach out to a target.
#
#   Each creature grows from the same base.
#
#   The target can be moved at any time to a random
#   location by pressing 'space'
#
#   Pressing 'w' toggles visibility of entire population
#   vs. just the winner.
#
# ===================================

import pygame.gfxdraw

from creature import Creature
from target import Target
from random import randrange
import math

# Setup screen
WIDTH = 1024
HEIGHT = 768
SIZE = (WIDTH, HEIGHT)
TITLE = "Stick Creatures - Tentacles"
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Startup
pygame.init()
pygame.display.set_caption(TITLE)
screen = pygame.display.set_mode(SIZE)
done = False

# Simulation variables
population = 50                     # number of creatures to spawn
creatures = []                      # array of creatures
n_gens = 0                          # number of generations
BEST_D_RESET = 9999                 # impossible number for distance reset
best_distance = BEST_D_RESET        # best distance attained by population
best = 0                            # index of creature with closest distance
distance = 0                        # distance to target
target = Target(screen, 200, 200)   # target
show_best = True                    # toggle for showing entire population vs only the winner


def dislpay_instructions():
    font = pygame.font.Font(None, 26)
    txt = "Press [SPACE] to move target.  Press [W] to toggle showing the only winner vs. the entire population"
    render = font.render(txt, 0, WHITE, BLACK)
    screen.blit(render, (110, 730))


# create creatures and target
for i in range(population):
    creatures.append(Creature(screen))

# Main loop
while not done:
    screen.fill(BLACK)
    n_gens += 1

    # reset breeding variables
    best_distance = BEST_D_RESET
    best = 0

    # Creature wins if it is closest to target
    for i in range(len(creatures)):
        distance = math.sqrt(abs(creatures[i].get_loc()[1] - target.get_loc()[1]) ** 2 +
                             abs(creatures[i].get_loc()[0] - target.get_loc()[0]) ** 2)
        if distance < best_distance:
            best_distance = distance
            best = i

    # Breed
    for i in range(len(creatures)):
        if i != best:
            creatures[i].breedwith(creatures[best])

    # Draw the target
    target.draw()

    dislpay_instructions()

    # Update and draw creature
    for i in range(len(creatures)):
        creatures[i].update()

    # show only the winner or the entire population
    if show_best:
        creatures[best].draw()
    else:
        for i in range(len(creatures)):
            creatures[i].draw()

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE or event.key == pygame.K_q:
                done = True
            elif event.key == pygame.K_SPACE:
                target.y = randrange(1, HEIGHT-200)
            elif event.key == pygame.K_w:
                show_best = not show_best

    pygame.display.flip()
pygame.quit()
