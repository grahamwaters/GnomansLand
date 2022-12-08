import numpy as np
import pygame
import random
from gnome import Gnome
from environment import Environment
from policies import get_reward
# Create the environment.
environment = Environment(10, 10, 64) # 10x10 tiles, each 64x64 pixels

# Create the gnome.
gnome = Gnome(0, 0) # start at the top-left corner of the environment

# Create the game window.
pygame.init()

# Set the window title.
pygame.display.set_caption("Gnome's Land")

# Create the screen surface.
screen = pygame.display.set_mode((environment.width * environment.tile_size, environment.height * environment.tile_size))

# Create a clock to control the game's framerate.
clock = pygame.time.Clock()