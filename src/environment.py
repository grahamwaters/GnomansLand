import numpy as np
import pygame
import random

class Environment:
    """
    The Environment class represents the game world and its objects and features.
    The Environment class has the following attributes and methods:
        width: The width of the environment, in tiles.
        height: The height of the environment, in tiles.
        tile_size: The size of each tile, in pixels.
        tiles: A 2D array of tiles representing the game world.
        __init__(): The constructor for the Environment class. This method initializes the environment with the specified width, height, and tile size, and creates an empty array of tiles.
        create(): This method generates the tiles for the game world.
    """
    tile_colors = {
        0: (0, 0, 0),  # Black for empty tiles
        1: (0, 255, 0),  # Green for forest tiles
        2: (0, 0, 255),  # Blue for water tiles
        3: (255, 255, 0),  # Yellow for grassland tiles
        4: (128, 128, 128),  # Grey for rocky dirt tiles
        5: (255, 0, 0),  # Red for mountain tiles
    }
    def __init__(self, width: int, height: int, tile_size: int):
        """
        Initialize the environment with the specified width, height, and tile size.

        :param width: The width of the environment, in tiles.
        :param height: The height of the environment, in tiles.
        :param tile_size: The size of each tile, in pixels.
        """

        # Store the dimensions of the environment and the tile size.
        self.width = width
        self.height = height
        self.tile_size = tile_size
        self.agent_x = None
        self.agent_y = None

        # Create an array of tiles to represent the game world.
        self.tiles = np.zeros((width, height), dtype=np.int8)

    def get_agent_position(self):
        """
        Get the current position of the agent in the environment.

        :return: A tuple (x, y) containing the x- and y-coordinates of the agent.
        """

        return (self.agent_x, self.agent_y)

    def set_agent_position(self, x: int, y: int):
        """
        Set the position of the agent in the environment.

        :param x: The x-coordinate of the agent's new position.
        :param y: The y-coordinate of the agent's new position.
        """

        self.agent_x = x
        self.agent_y = y


    def create(self):
        """
        Create the game world by randomly generating the tiles.

        For the create() method, you can use random numbers to generate the tiles for the game world. You can define a dictionary that maps tile types to color values, and use this dictionary to assign a color to each tile based on its type.
        """

        # Define probabilities for each tile type.
        tile_probs = {
            0: 0,  # Empty tiles
            1: 0.5,  # Forest tiles
            2: 0.1,  # Water tiles
            3: 0.1,  # Grassland tiles
            4: 0.1,  # Rocky dirt tiles
            5: 0.1,  # Mountain tiles
        }
        # Check that the tile probabilities add up to 1.
        assert abs(sum(tile_probs.values()) - 1.0) < 1e-6

        # initial placement of agent
        # Generate the initial position of the agent.
        agent_x = random.randint(0, self.width - 1)
        agent_y = random.randint(0, self.height - 1)

        # Set the tile at the agent's initial position to be empty.
        self.tiles[agent_x, agent_y] = 0

        # Create the water tiles by using the np.ones() function to create a border of water tiles around the environment.
        self.tiles[0, :] = np.ones((1, self.height), dtype=np.int8)
        self.tiles[-1, :] = np.ones((1, self.height), dtype=np.int8)
        self.tiles[:, 0] = np.ones((self.width, 1), dtype=np.int8)
        self.tiles[:, -1] = np.ones((self.width, 1), dtype=np.int8)

        # Create the remaining tiles by randomly setting each tile to a type based on the tile probabilities.
        for i in range(self.width):
            for j in range(self.height):
                if self.tiles[i, j] == 0:
                    tile_type = random.choices(list(tile_probs.keys()), weights=list(tile_probs.values()))[0]
                    self.tiles[i, j] = tile_type

    def get_tile(self, x: int, y: int) -> int:
        """
        Get the tile at the specified position.

        :param x: The x-coordinate of the tile.
        :param y: The y-coordinate of the tile.
        :return: The tile at the specified position.
        """

        return self.tiles[x, y]

    def set_tile(self, x: int, y: int, tile: int):
        """
        Set the tile at the specified position.

        :param x: The x-coordinate of the tile.
        :param y: The y-coordinate of the tile.
        :param tile: The tile to set.
        """

        self.tiles[x, y] = tile


    def render(self, screen: pygame.Surface):
        """
        Render the game world to the specified screen.
        For the render() method, you can use Pygame's draw.rect() method to draw the tiles to the screen. You will need to iterate over the tiles in the game world and draw a rectangle for each tile at the correct position.

        :param screen: The screen to render the game world to.
        """
        # Iterate over the tiles in the game world and draw a rectangle for each tile at the correct position.
        for x, y in np.ndindex(self.tiles.shape):
            # Get the color of the tile.
            color = self.tile_colors[self.tiles[x, y]]

            # Create a rectangle for the tile at the correct position and with the correct color.
            rect = pygame.Rect(x * self.tile_size, y * self.tile_size, self.tile_size, self.tile_size)
            pygame.draw.rect(screen, color, rect)