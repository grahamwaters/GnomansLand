import pygame
import random
from gnome import Gnome
from environment import Environment
from policies import get_reward
from game import Game



# Create the environment.
environment = Environment(10, 10, 64) # 10x10 tiles, each 64x64 pixels

# Create the gnome.
gnome = Gnome(0, 0) # start at the top-left corner of the environment

# Create the game.
game = Game(environment, gnome)

# Run the game.
game.run()
