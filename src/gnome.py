import numpy as np
import pygame
import random

class Gnome:
    """
        The Gnome class represents the gnome agent in the game.
        The Gnome class has the following attributes and methods:
            x: The x-coordinate of the gnome's position.
            y: The y-coordinate of the gnome's position.
            carrying: The type of item the gnome is currently carrying. This can be None if the gnome is not carrying any items.
            __init__(): The constructor for the Gnome class. This method initializes the gnome with a starting position and sets carrying to None.
            move(): This method moves the gnome to a new position in the game world.
            act(): This method is called when the gnome needs to take an action in the game world, such as moving or picking up an item.
            render(): This method renders the gnome to the screen.
    """
    def __init__(self, x: int, y: int):
        """
        Initialize the gnome with the specified starting position.

        :param x: The x-coordinate of the gnome's starting position.
        :param y: The y-coordinate of the gnome's starting position.
        """
        self.x = x
        self.y = y
        self.carrying = None # the gnome is not carrying anything

    def move(self, dx: int, dy: int):
        """
        Move the gnome to a new position in the game world.

        :param dx: The change in x-coordinate.
        :param dy: The change in y-coordinate.
        """
        self.x += dx # move the gnome in the x direction by dx
        self.y += dy # move the gnome in the y direction by dy

    def act(self, environment: "Environment"):
        """
        Perform an action in the environment.
        The gnome can perform the following actions:
            - Move in one of the four cardinal directions (up, down, left, or right).
            - Pick up an object from its current location if there is one present.
            - Drop an object at its current location if it is carrying one.
        """
        # Get the tile at the gnome's current location.
        tile = environment.get_tile(self.x, self.y)

        # If the gnome is carrying an object, try to drop it.
        if self.carrying is not None:
            # If the tile is empty, drop the object.
            if tile == 0:
                environment.set_tile(self.x, self.y, self.carrying)
                self.carrying = None
            # Otherwise, move in a random direction.
            else:
                dx = random.choice([-1, 0, 1])
                dy = random.choice([-1, 0, 1])
                self.move(dx, dy)

        # If the gnome is not carrying an object, try to pick one up.
        else:
            # If the tile is not empty, pick up the object.
            if tile != 0:
                self.carrying = tile
                environment.set_tile(self.x, self.y, 0)
            # Otherwise, move in a random direction.
            else:
                dx = random.choice([-1, 0, 1])
                dy = random.choice([-1, 0, 1])
                self.move(dx, dy)

        def render(self, screen: pygame.Surface, tile_size: int):
            """
            Render the gnome on the screen.
            For the render() method, you can use Pygame's draw.circle() method to draw the gnome as a circle.
            You will need to calculate the position of the gnome on the screen based on its x and y coordinates and the size of the tiles.

            :param screen: The screen to render the gnome to.
            :param tile_size: The size of each tile, in pixels.
            """
            # Calculate the position of the gnome on the screen.
            x_pos = self.x * tile_size
            y_pos = self.y * tile_size

            # Draw the gnome as a circle.
            pygame.draw.circle(screen, (255, 255, 0), (x_pos, y_pos), tile_size // 2)
