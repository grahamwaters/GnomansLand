import numpy as np
import pygame

import random
from collections import defaultdict
from gnome import Gnome
from environment import Environment
from policies import get_reward

# Initialize Pygame.
pygame.init()

# Set the size of the screen.
screen_width = 800
screen_height = 600
# Create the game world.
tile_size = 32


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
        self.y = y  # * note: this y is defined.
        self.carrying = None  # the gnome is not carrying anything

    def move(self, dx: int, dy: int):
        """
        Move the gnome to a new position in the game world.

        :param dx: The change in x-coordinate.
        :param dy: The change in y-coordinate.
        """
        self.x += dx  # move the gnome in the x direction by dx
        self.y += dy  # move the gnome in the y direction by dy

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
                self.random_move()

        # If the gnome is not carrying an object, try to pick one up.
        else:
            # If the tile is not empty, pick up the object.
            if tile != 0:
                self.carrying = tile
                environment.set_tile(self.x, self.y, 0)
            # Otherwise, move in a random direction.
            else:
                self.random_move()

    def random_move(self):
        """
        Move the gnome in a random direction.
        """
        dx = random.choice([-1, 0, 1])
        dy = random.choice([-1, 0, 1])
        self.move(dx, dy)

    def render(self, screen: pygame.Surface, tile_size: int):
        """
        Render the gnome on the screen.

        :param screen: The screen to render the gnome to.
        :param tile_size: The size of each tile, in pixels.
        """
        # Calculate the position of the gnome on the screen.
        x_pos = self.x * tile_size
        y_pos = self.y * tile_size

        # Draw the gnome as a circle with a fixed size.
        gnome_size = 10
        pygame.draw.circle(screen, (255, 255, 0), (x_pos, y_pos), gnome_size)


class Agent:
    """
    The Agent class represents an agent that uses reinforcement learning to learn a policy for the gnome to follow.
    The Agent class has the following attributes and methods:
        policy: A dictionary that maps state-action pairs to probabilities of taking the action in the state.
        alpha: The learning rate used in the learning algorithm.
        gamma: The discount factor used in the learning algorithm.
        epsilon: The exploration rate used in the learning algorithm.
        __init__(): The constructor for the Agent class. This method initializes the agent with default values for the policy, learning rate, discount factor, and exploration rate.
        act(): This method is called when the agent needs to take an action in the environment. It uses the learned policy to determine the action to take.
        learn(): This method is called when the agent experiences a reward in the environment. It updates the policy based on the reward.
    """

    def __init__(self):
        """
        Initialize the agent with default values for the policy, learning rate, discount factor, and exploration rate.
        """
        self.policy = defaultdict(lambda: defaultdict(int))
        self.alpha = 0.1
        self.gamma = 0.9
        self.epsilon = 0.1
        pass

    def act(self, state: int) -> int:
        # If the agent should explore, choose a random action.
        if random.random() < self.epsilon:
            return random.randint(0, 3)

        # Otherwise, choose the action with the highest probability in the policy.
        else:
            return max(self.policy[state], key=self.policy[state].get)

    def learn(self, state: int, action: int, gnome: Gnome):
        # Get the reward for the given state and action
        reward = get_reward(state, action, gnome)

        # Update the policy for the state-action pair.
        self.policy[state][action] += self.alpha * (
            reward
            - self.policy[state][action]
            + self.gamma * max(self.policy[state].values())
        )

        # Update the policy for the state-action pairs that lead to the state.
        for s in self.policy:
            for a in self.policy[s]:
                self.policy[s][a] += self.alpha * (
                    reward
                    - self.policy[s][a]
                    + self.gamma * max(self.policy[state].values())
                )

        # Update the policy for the state-action pairs that lead to the state-action pairs that lead to the state.
        for s in self.policy:  # for each state
            for a in self.policy[s]:  # for each action in the state
                for (
                    s2
                ) in (
                    self.policy
                ):  # for each state that leads to the state and action pair
                    for a2 in self.policy[
                        s2
                    ]:  # for each action in the state that leads to the state and action pair
                        # Create a new Gnome instance with the same x and y coordinates as the given gnome
                        new_gnome = Gnome(gnome.x, gnome.y)
                        self.policy[s2][a2] += self.alpha * (
                            reward
                            - self.policy[s2][a2]
                            + self.gamma * max(self.policy[state].values())
                        )  # update the policy for the state-action pair that leads to the state-action pair that leads to the state-action pair that leads to the state and action pair that leads to the state and action pair with the reward received for taking the action in the state.


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
                    tile_type = random.choices(
                        list(tile_probs.keys()), weights=list(tile_probs.values())
                    )[0]
                    self.tiles[i, j] = tile_type

    def get_tile(self, x: int, y: int):
        """
        Get the tile at the specified position.

        :param x: The x-coordinate of the tile.
        :param y: The y-coordinate of the tile.
        :return: The tile at the specified position.
        """
        if x < 0 or x >= self.width or y < 0 or y >= self.height:
            return None

        return self.tiles[x, y]

    def set_tile(self, x: int, y: int, tile: int):
        """
        Set the tile at the specified position.

        :param x: The x-coordinate of the tile.
        :param y: The y-coordinate of the tile.
        :param tile: The tile to set.
        """
        if x < 0 or x >= self.width or y < 0 or y >= self.height:
            return None
        self.tiles[x, y] = tile

    def render(self, screen: pygame.Surface, tile_size: int):
        """
        Render the environment to the screen.

        Copy code
        :param screen: The screen to render the environment to.
        :param tile_size: The size of each tile, in pixels.
        """
        # Iterate over each tile in the environment.
        for i in range(self.width):
            for j in range(self.height):
                # Get the type of the tile at the current position.
                tile = self.get_tile(i, j)

                # Calculate the position of the tile on the screen.
                x_pos = i * tile_size


class Policies:
    def __init__(self):
        pass

    def get_reward(self, state: np.ndarray, action: int):
        if action == 0:  # move left
            if state[0, 1] == 2:  # water
                return -1.0
            elif state[0, 1] == 5:  # mountain
                return -0.5
            else:
                return 0.0
        elif action == 1:  # move right
            if state[0, 1] == 2:  # water
                return -1.0
            elif state[0, 1] == 5:  # mountain
                return -0.5
            else:
                return 0.0
        elif action == 2:  # move up
            if state[0, 1] == 2:  # water
                return -1.0
            elif state[0, 1] == 5:  # mountain
                return -0.5
            else:
                return 0.0
        elif action == 3:  # move down
            if state[0, 1] == 2:  # water
                return -1.0
            elif state[0, 1] == 5:  # mountain
                return -0.5
            else:
                return 0.0


class Game:
    def __init__(self, environment: Environment, gnome: Gnome):
        self.environment = environment
        self.gnome = gnome

    def update(self):
        """
        update the game state.

        """
        self.gnome.act(self.environment)  # perform an action in the environment

    def render(self):
        """
        render the game world to the screen.

        :param screen: The screen to render the game world to.
        """
        self.environment.render(screen, tile_size)

    def process_input(self):
        # Process user input, such as keyboard or mouse events.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # If the user presses the spacebar, reset the game.
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.reset()

    def reset(self):
        # Reset the game state.
        self.environment.reset()
        self.gnome.reset()

    def run(self):
        # Run the game loop, which updates the game state, renders the game world, and processes user input.
        while True:
            self.update()  # update the game state
            self.render()  # render the game world
            #!self.process_input() # process user input
            clock.tick(60)  # limit the framerate to 60 frames per second


screen = pygame.display.set_mode((screen_width, screen_height))

# Set the title of the window.
pygame.display.set_caption("Gnomansland")

# Create a clock to limit the framerate.
clock = pygame.time.Clock()


# Create the game world.
environment = Environment(20, 15, tile_size)

# Create the gnome.
x_value = environment.width // 2
y_value = environment.height // 2

gnome = Gnome(x_value, y_value)


# Create the game.
game = Game(environment, gnome)

# Run the game loop.
game.run()
