import gym
import numpy as np
import random

# class Agent():
    # ...

class Gnome:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
        self.carrying = None
        self.is_dead = False

    def move(self, direction: str):
        if direction == "left":
            self.x -= 1
        elif direction == "right":
            self.x += 1
        elif direction == "up":
            self.y -= 1
        elif direction == "down":
            self.y += 1

    def act(self, environment):
        actions = ["left", "right", "up", "down"]
        action = random.choice(actions)
        self.move(action)

    def render(self, screen):
        pygame.draw.rect(screen, (255, 0, 0), (self.x, self.y, 32, 32))

class Environment:
    def __init__(self, width: int, height: int, tile_size: int, gnome: Gnome):
        self.width = width
        self.height = height
        self.tile_size = tile_size
        self.gnome = gnome
        self.gnome_x = random.randint(0, self.width - 1)
        self.gnome_y = random.randint(0, self.height - 1)
        self.tiles = np.zeros((width, height), dtype=np.int8)
        self.step_count = 0
    def get_state(self, gnome: Gnome):
        return (self.gnome_x, self.gnome_y, self.tiles[self.gnome_x, self.gnome_y])
    def create(self, gnome: Gnome):
        tile_probs = {
            0: 0,
            1: 0.5,
            2: 0.1,
            3: 0.1,
            4: 0.1,
            5: 0.1,
        }
        self.tiles = np.random.choice(
            list(tile_probs.keys()),
            size=(self.width, self.height),
            p=list(tile_probs.values()),
        )



import gym
import numpy as np
from gym import spaces

# Define the action space and observation space for the environment.
action_space = spaces.Discrete(4)  # 0: left, 1: right, 2: up, 3: down
observation_space = spaces.Box(
    low=0, high=255, shape=(height, width, 3), dtype=np.uint8
)



class GnomanslandEnv(gym.Env):
    """
    The GnomanslandEnv class represents the game world and its objects and features.
    The GnomanslandEnv class has the following attributes and methods:
        width: The width of the environment, in tiles.
        height: The height of the environment, in tiles.
        gnome: An instance of the Gnome class.
        tiles: A 2D array of tiles representing the game world.
        __init__(): The constructor for the GnomanslandEnv class. This method initializes the environment with the specified width, height, and tile size, and creates an empty array of tiles.
        create(): This method generates the tiles for the game world.
        step(): This method takes an action and updates the environment.
        render(): This method renders the environment to the screen.
        close(): This method closes the environment.
    """

    metadata = {"render.modes": ["human"]}

    def __init__(self, width: int, height: int, tile_size: int, gnome: Gnome):
        """
        Initialize the environment with the specified width, height, and tile size.

        :param width: The width of the environment, in tiles.
        :param height: The height of the environment, in tiles.
        :param tile_size: The size of each tile, in pixels.
        :param gnome: An instance of the Gnome class.
        """

        # Store the dimensions of the environment and the tile size.
        self.width = width
        self.height = height
        self.tile_size = tile_size

        # Initialize the gnome and place it randomly in the environment.
        self.gnome = gnome
        self.gnome_x = random.randint(0, self.width - 1)
        self.gnome_y = random.randint(0, self.height - 1)

        # Create an array of tiles to represent the game world.
        self.tiles = np.zeros((width, height), dtype=np.int8)
        self.step_count = 0  # keep track of the number of steps taken by the gnome

    def create(self):
        """
        Create the game world by randomly generating the tiles.

        For the create() method, you can use random numbers to generate the tiles for the game world. You can define a dictionary that maps tile types to color values, and use this dictionary to assign a color to each tile based on its type.
        """
        # DEFINE RANDOM TILES WITH PROBABILITIES
        # Generate random probabilities that sum up to 1.
        tile_probs = np.random.dirichlet(np.ones(6))

        # Generate the tiles for the game world.
        self.tiles = np.random.choice(
            [1, 2, 3, 4, 5, 6], size=(self.width, self.height), p=tile_probs
        )

    def render(self, screen):
        # Draw the tiles.
        for x in range(self.width):
            for y in range(self.height):
                tile_type = self.tiles[x, y]
                color = TILE_COLORS[tile_type]
                pygame.draw.rect(
                    screen, color, (x * self.tile_size, y * self.tile_size, self.tile_size, self.tile_size)
                )

        # Draw the gnome.
        self.gnome.render(screen) # this is the line that calls the gnome's render method




    def step(self, action):
        # Perform the specified action and return the resulting state, reward and done flag.
        self.gnome.act(self.environment, action)

        # Get the current state of the environment.
        state = self.environment.get_state()

        # Calculate the reward based on the state.
        reward = ...

        # Check if the game is over.
        done = ...

        # Return the state, reward, and done flag.
        return state, reward, done, {}

    def reset(self):
        """
        Reset the environment to its initial state.

        :return: The initial state of the environment.
        """

        # Place the gnome at a random position in the environment.
        self.gnome_x = random.randint(0, self.width - 1)
        self.gnome_y = random.randint(0, self.height - 1)

        # Place the goal at a random position in the environment.
        self.goal_x = random.randint(0, self.width - 1)
        self.goal_y = random.randint(0, self.height - 1)

        # Reset the step count.
        self.step_count = 0

        # Return the initial state of the environment.
        return self.get_state()



# Create an instance of the Gnomansland environment.
env = Gnomansland()

# Reset the environment to get the initial state.
state = env.reset()

# Perform some actions and get the resulting state, reward, and done flag.
state, reward, done, _ = env.step(0)
state, reward, done, _ = env.step(1)
state, reward, done, _ = env.step(2)

# # Check if the game is over.
# if done:
#     # end the game
#     quit()


# Here is an outline for the rest of the project:

# Create the Gnome class and implement its init(), move(), act(), and render() methods.
# Create the Environment class and implement its init(), create(), get_state(), and set_agent_position() methods.
# Implement the Q-learning algorithm in the Gnome class by adding the q_learning_policy(), q_learning_update(), and q_learning_train() methods.
# In the Environment class, add a draw() method to render the game world to the screen.
# In the main() function, initialize the environment and the gnome and start the game loop. In each iteration of the loop, call the gnome's act() method to let it take an action in the environment, and call the environment's draw() method to render the game world to the screen.
# Test the game by playing it manually and by running the Q-learning algorithm to train the gnome.
# Continue refining and testing the game until it is functioning as desired.