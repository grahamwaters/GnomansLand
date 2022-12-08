import pygame

"""
This code uses Pygame to create a 2D array of tiles representing the game world, and then draws these tiles to the screen using the specified biome colors. You can modify the code to specify the probability distribution of biomes in the game world, and to create different shapes and patterns of biomes in the game world. You can also add additional objects and features to the game world, such as the cave,
"""


# Set the screen dimensions and initialize Pygame.
SCREEN_WIDTH = 100
SCREEN_HEIGHT = 100
pygame.init()

# Create the screen surface and set the title.
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Gnoman's Land")

# Create a dictionary of colors for the different biomes in the game world.
biome_colors = {
    "forest": (34, 139, 34),  # Dark green
    "lake": (0, 191, 255),  # Deep sky blue
    "grassland": (124, 252, 0),  # Lawn green
    "rocky_dirt": (255, 222, 173),  # Navajo white
    "mountains": (139, 69, 19)  # Saddle brown
}

# Create a 2D array of tiles representing the game world.
tiles = []
for i in range(SCREEN_WIDTH):
    row = []
    for j in range(SCREEN_HEIGHT):
        # Choose a random biome for each tile based on the probability distribution of biomes in the game world.
        biome = choose_biome()
        row.append(biome)
    tiles.append(row)

# Draw the game world to the screen using the tile array and the biome colors.
for i in range(SCREEN_WIDTH):
    for j in range(SCREEN_HEIGHT):
        biome = tiles[i][j]
        color = biome_colors[biome]
        pygame.draw.rect(screen, color, (i * 10, j * 10, 10, 10))

# Update the screen to display the game world.
pygame.display.flip()
