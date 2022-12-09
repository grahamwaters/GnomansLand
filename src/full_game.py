import numpy as np
import pygame
import sys
import random
from collections import defaultdict
from typing import List, Tuple, Any
import time


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

    def __init__(self, x: int, y: int, environment):
        """
        Initialize the gnome with the specified starting position.

        :param x: The x-coordinate of the gnome's starting position.
        :param y: The y-coordinate of the gnome's starting position.
        """
        self.x = x
        self.y = y  # * note: this y is defined.
        self.carrying = None  # the gnome is not carrying anything
        self.max_reward = 100  # the maximum reward for reaching the item
        self.min_reward = 1  # the minimum reward for not reaching the item, or for some action taken by the agent (gnome) in the environment that improves their chance of survival.
        self.min_punishment = (
            -1
        )  # the minimum punishment for not reaching the item, or for some action taken by the agent (gnome) in the environment.
        self.max_punishment = (
            -10
        )  # the maximum punishment for some action taken by the agent (gnome) in the environment.
        self.is_dead = False  # the gnome is not dead yet
        self.gamma = 0.9  # the discount factor for the Bellman equation
        self.environment = environment  # the environment the gnome is in

    # * Reinforcement Learning Methods
    def q_learning_policy(
        self, state: np.ndarray, actions, environment
    ):  # -> int:
        # Initialize the Q-values for each action to 0.
        q_values = defaultdict(lambda: 0)

        # Loop through each valid action.
        for action in actions:
            # Get the next state and reward if the gnome takes the current action.
            next_state, reward, is_done = self.environment.step(action, state) # * note: this is the environment.step() method, not the gnome.step() method.
            if is_done:
                # If the gnome has reached the goal, set the Q-value for the current action to the reward.
                q_values[action] = reward
                continue
            # Calculate the Q-value for the current action using the Bellman equation.
            # Q(s, a) = reward + gamma * max(Q(s', a'))
            q_values[action] = reward + self.gamma * max(
                q_values[next_state, a]
                for a in self.environment.get_valid_actions(next_state)
            )

        # Choose the action with the highest Q-value.
        best_action = max(q_values, key=q_values.get)

        return best_action


        return best_action

    def has_reached_goal(self, new_state: np.ndarray):  # -> bool:
        """
        Check if the gnome has reached the goal in the new state.

        :param new_state: The new state of the environment.
        :return: True if the gnome has reached the goal, False otherwise.
        """
        # Get the indices of all the elements in new_state that have a value of 2.
        goal_indices = np.argwhere(new_state == 2)

        # Check if the gnome's current position is one of the goal indices.
        if (self.x, self.y) in goal_indices:
            # Return True if the gnome's current position is a goal index.
            return True
        else:
            # Return False if the gnome's current position is not a goal index.
            return False

    def reset(self):
        """
        Reset the gnome to its starting position.
        """
        self.carrying = None

    def move(self, dx: int, dy: int):
        """
        Move the gnome to a new position in the game world.

        :param dx: The change in x-coordinate.
        :param dy: The change in y-coordinate.
        """
        self.x += dx  # move the gnome in the x direction by dx
        self.y += dy  # move the gnome in the y direction by dy

    def act(self, state: np.ndarray, environment: "Environment"):
        # Get the valid actions in the current state.
        actions = environment.get_valid_actions(state)

        # Use the Q-learning policy to choose the best action.
        action = self.q_learning_policy(state, actions, environment)

        return action # * note: this is the action that the gnome takes in the environment.

    def get_valid_actions(self, state: np.ndarray):# -> List[int]:
        """
        Get the valid actions that the gnome can take in the current state.

        :param state: The current state of the environment.
        :return: A list of valid actions that the gnome can take in the current state.
        """
        # Get the x and y coordinates of the gnome's current position.
        x, y, _ = state

        # Define the possible actions that the gnome can take.
        actions = [0, 1, 2, 3]  # 0 = move left, 1 = move right, 2 = move up, 3 = move down

        # Check if moving left would take the gnome out of bounds.
        if x == 0:
            # Remove the action for moving left from the list of possible actions.
            actions.remove(0)

        # Check if moving right would take the gnome out of bounds.
        if x == self.environment.width - 1:
            # Remove the action for moving right from the list of possible actions.
            actions.remove(1)

        # Check if moving up would take the gnome out of bounds.
        if y == 0:
            # Remove the action for moving up from the list of possible actions.
            actions.remove(2)

        # Check if moving down would take the gnome out of bounds.
        if y == self.environment.height - 1:
            # Remove the action for moving down from the list of possible actions.
            actions.remove(3)

        # Return the list of valid actions.
        return actions


    def random_move(self):
        """
        Move the gnome in a random direction.
        """
        dx = random.choice([-1, 0, 1])
        dy = random.choice([-1, 0, 1])
        self.move(dx, dy)
        return dx, dy

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

    def get_reward(self, state: np.ndarray, reached_item: bool):  # -> int:
        """
        Calculate the reward for the given state.
        :param state: The state of the environment.
        :param reached_item: A flag indicating whether the gnome has reached the item.
        :return: The reward for the given state.
        """
        # If the gnome has reached the item, return the maximum reward.
        if reached_item:
            return self.max_reward
        else:
            return self.min_punishment
        # Otherwise, return 0.
        return 0


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

    def act(self, state: np.ndarray):
        # Get the valid actions that the gnome can take in the current state.
        actions = self.environment.get_valid_actions(state)

        # Use the Q-learning policy to determine the next action for the gnome.
        action = self.q_learning_policy(state, actions)

        # Take the action determined by the Q-learning policy.
        self.move(*action)

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

    # ^ The "Gets"

    def get_agent_position(self):
        """
        Get the current position of the agent in the environment.

        :return: A tuple (x, y) containing the x- and y-coordinates of the agent.
        """

        return (self.gnome_x, self.gnome_y)

    def get_state(self, gnome: Gnome):
        """
        Get the current state of the environment.

        :return: A tuple containing the current position of the agent and the type of tile it is on.
        """

        return (
            self.gnome_x,
            self.gnome_y,
            self.tiles[self.gnome_x, self.gnome_y],
        )  # return the state

    def set_agent_position(self, x: int, y: int):
        """
        Set the position of the agent in the environment.

        :param x: The x-coordinate of the agent's new position.
        :param y: The y-coordinate of the agent's new position.
        """

        self.gnome_x = x
        self.gnome_y = y

    def create(self, gnome: Gnome):
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
        #!assert abs(sum(tile_probs.values()) - 1.0) < 1e-6

        # Generate the tiles for the game world.
        for x in range(self.width):
            for y in range(self.height):
                # Generate a random number between 0 and 1.
                r = random.random()

                # Set the tile type based on the probabilities.
                if r < tile_probs[1]:
                    self.tiles[x, y] = 1  # Forest tile
                elif r < tile_probs[1] + tile_probs[2]:
                    self.tiles[x, y] = 2  # Water tile
                elif r < tile_probs[1] + tile_probs[2] + tile_probs[3]:
                    self.tiles[x, y] = 3  # Grassland tile
                elif r < tile_probs[1] + tile_probs[2] + tile_probs[3] + tile_probs[4]:
                    self.tiles[x, y] = 4  # Rocky dirt tile
                else:
                    self.tiles[x, y] = 5  # Mountain tile

        # Place the gnome in the environment.
        self.gnome_x = random.randint(0, self.width - 1)
        self.gnome_y = random.randint(0, self.height - 1)

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

    def get_item_position(self):
        """
        Get the position of the item in the game world.

        :return: The x- and y-coordinates of the item.
        """
        # Find the x- and y-coordinates of the item in the game world.
        item_x, item_y = np.where(self.tiles == 1)

        # Return the position of the item.
        return item_x[0], item_y[0]

    def get_item_positions(self):
        item_positions = []
        for x in range(self.width):
            for y in range(self.height):
                if self.tiles[x, y] in (1, 2, 3, 4, 5):
                    item_positions.append((x, y))
        return item_positions

    def get_state(self, gnome: Gnome):
        """
        Get the current state of the environment.

        :return: A tuple containing the current position of the agent and the type of tile it is on.
        """

        return (
            self.gnome_x,
            self.gnome_y,
            self.tiles[self.gnome_x, self.gnome_y],
        )  # return the state as a tuple



    def get_state_space(self, state: np.ndarray):  # -> np.ndarray:
        """
        Get the state space of the environment from the current state.

        :param state: The current state of the environment.
        :return: The state space of the environment.
        """
        # Initialize the state space with zeros.
        state_space = np.zeros((self.height, self.width))

        # Get the x- and y-coordinates of the agent.
        x, y = state[0], state[1]

        # Set the state space to 1 for the current position of the agent.
        state_space[y, x] = 1

        # Return the state space.
        return state_space

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

    def reset(self):
        """
        Reset the environment to its initial state.

        :return: The initial state of the environment.
        """
        # Create the game world.
        self.create()

        # Set the agent's initial position.
        self.set_agent_position(self.gnome_x, self.gnome_y)

        # Get the initial state of the environment.
        state = self.get_state()

        return state

    def update(self, new_state: np.ndarray, environment: np.ndarray):
        """
        Update the state of the game world.

        :param new_state: The new state of the game world.
        """
        # Get the current state of the game world.
        state = self.get_state()  # -> np.ndarray

        # Get the agent's current position.
        gnome_x, gnome_y = environment.get_agent_position()

        # Get the agent's new position.
        new_gnome_x = new_state[0] // environment.width
        new_gnome_y = new_state[0] % environment.width

        # Get the item's new position.
        new_item_x = new_state[1] // environment.width
        new_item_y = new_state[1] % environment.width

        # Move the agent to its new position.
        environment.set_tile(gnome_x, gnome_y, 0)
        environment.set_tile(new_gnome_x, new_gnome_y, 6)

        # Move the item to its new position.
        environment.set_tile(new_item_x, new_item_y, 1)

    def get_valid_actions(self, state: np.ndarray):
        # Get the agent's current position.
        gnome_x, gnome_y = self.get_agent_position()

        # Get the tile at the agent's current position.
        tile = self.get_tile(gnome_x, gnome_y)

        # Determine the valid actions for the current state.
        valid_actions = []
        if gnome_x > 0:
            # The agent can move left if it is not at the left edge of the grid.
            valid_actions.append(0)
        if gnome_x < self.width - 1:
            # The agent can move right if it is not at the right edge of the grid.
            valid_actions.append(1)
        if gnome_y > 0:
            # The agent can move up if it is not at the top edge of the grid.
            valid_actions.append(2)
        if gnome_y < self.height - 1:
            # The agent can move down if it is not at the bottom edge of the grid.
            valid_actions.append(3)

        # Return the valid actions for the current state.
        return valid_actions

    def step(self, action: int, gnome: Gnome):
        """
        Take a step in the environment by applying the specified action.

        :param action: The action to take.
        :param gnome: An instance of the Gnome class.
        :return: A tuple containing the new state, the reward, and a flag indicating whether the game is over.
        """
        # Apply the action to the environment.
        #new_state = self.apply_action(action, gnome) # this returns the new state, reward, and is_done flag
        new_state, reward, is_done = self.apply_action(action, gnome)[:3]

        # Return the new state, reward, and is_done flag.
        return new_state, reward, is_done # this has the reward set as 0.0


    def apply_action(self, action, gnome):
        # Apply the action to the environment.
        x, y, tile = self.get_state(gnome)
        # Update the position of the agent in the environment.
        if action == 0:  # move left
            x -= 1
        elif action == 1:  # move right
            x += 1
        elif action == 2:  # move up
            y -= 1
        elif action == 3:  # move down
            y += 1
        # Check if the agent has moved out of bounds.
        if x < 0 or x >= self.width or y < 0 or y >= self.height:
            return self.get_state(gnome), -1.0, True
        # Update the position of the agent in the environment.
        self.set_agent_position(x, y)
        # Return the new state, reward, and is_done flag.
        return self.get_state(gnome), 0.0, False



# create the parent class for the food and water
class Resource:
    def init(self, x, y):
        self.x = x
        self.y = y
        self.is_eaten = False # is the food/water eaten?
        self.is_drunk = False # is the water drunk?
        self.color = (0, 0, 0) # the color of the food/water (black)

# create the food class
class Food(Resource):
    def init(self, x, y):
        super().init(x, y)
        self.color = (255, 0, 0) # the color of the food (red)

# create the water class
class Water(Resource):
    def init(self, x, y):
        super().init(x, y)
        self.color = (0, 0, 255) # the color of the water (blue)

# create the tree class
class Tree(Resource):
    def init(self, x, y):
        super().init(x, y)
        self.color = (0, 255, 0) # the color of the tree (green)


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
    """
    Game The Game class is responsible for running the game loop. It will take the action returned by the agent, pass it to the environment, and then render the environment. It will also keep track of the score and the number of steps taken.

    _extended_summary_
    """
    def __init__(self, environment: Environment, gnome: Gnome):
        self.environment = environment
        self.gnome = gnome
        self.tile_size = 32  # the size of each tile, in pixels
        self.is_done = False  # when the game is over, set this to True

    def take_action(self, state, action):
        # Take the action in the environment.
        """
        take_action With this update, the take_action() method should be able to unpack the values returned by the step() method without any issues, and the main() function should be able to run without getting the ValueError.

        Alternatively, you could update the step() method of the Environment class to return four values instead of three. This would allow the take_action() method to unpack the values returned by the step() method without needing to be updated.



        _extended_summary_

        :param state: _description_
        :type state: _type_
        :param action: _description_
        :type action: _type_
        :return: _description_
        :rtype: _type_
        """
        new_state, reward, done = self.environment.step(action, self.gnome)

        # Return the new state, reward, and is_done flag.
        return new_state, reward, done

    def render(self, screen: pygame.Surface, environment: "Environment", gnome: Gnome):
        """
        This code defines a render() method for the Game class. This method takes three arguments: screen, environment, and gnome, which are the screen to render the game world to, the environment object containing the game world state, and the gnome object representing the agent in the game, respectively.

        The render() method first gets the current state of the environment using the environment.get_state() method. It then defines a dictionary colors that maps the different tile types to their corresponding colors.

        Next, the method loops through the state and renders each tile to the screen. For each tile at position (x, y), it gets the type of tile at that position and uses it to look up the corresponding color in the colors dictionary. It then calculates the screen coordinates for the tile, creates a rectangle object representing the tile, and draws the tile to the screen using the pygame.draw.rect() method.

        After rendering the tiles, the method gets the screen coordinates for the gnome, chooses the color for the gnome based on the type of item it is carrying, creates a rectangle object representing the gnome, and draws the gnome to the screen. Finally, it updates the screen using the pygame.display.flip() method.
        """
        # Get the current state of the environment.
        state = environment.get_state(gnome)
        state_space = environment.get_state_space(
            state
        )  # get the state space for the current state
        # state = state.reshape((environment.height, environment.width))
        colors = {
            0: (255, 255, 255),  # empty
            1: (255, 0, 0),  # gnome
            2: (0, 0, 255),  # water
            3: (0, 255, 0),  # grass
            4: (255, 255, 0),  # goal
            5: (0, 0, 0),  # mountain
            None: (128, 128, 128),  # gnome is not carrying anything
        }

        # Loop through the state and render each tile to the screen.
        for y in range(environment.height):
            for x in range(environment.width):
                # Get the type of tile at position (x, y).
                tile = state_space[y][x]

                # Get the screen coordinates for the tile.
                screen_x = x * tile_size
                screen_y = y * tile_size

                # Choose the color for the tile based on its type.
                color = colors[tile]

                # Create a rectangle for the tile.
                rect = pygame.Rect(screen_x, screen_y, tile_size, tile_size)

                # Draw the tile to the screen.
                pygame.draw.rect(screen, color, rect)

        # Get the screen coordinates for the gnome.
        screen_x = gnome.x * tile_size
        screen_y = gnome.y * tile_size

        # Choose the color for the gnome.
        color = colors[gnome.carrying]

        # Create a rectangle for the gnome.
        rect = pygame.Rect(screen_x, screen_y, tile_size, tile_size)

        # Draw the gnome to the screen.
        pygame.draw.rect(screen, color, rect)

        # Update the screen.
        pygame.display.flip()

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

    def run(self, screen, environment, gnome):
        """
        Run the game loop. This loop will run until the user exits the game.

        :param screen: The Pygame screen to render the game to.
        :param environment: The environment in which the game is played.
        :param gnome: The gnome agent that will be controlled by the player.
        """
        # Initialize the game state.
        state = environment.get_state()

        # Loop until the game is over.
        while not self.is_done:
            # Render the game state to the screen.
            self.render(screen, environment, gnome)

            # Check if the game is over.
            if self.is_done:
                break

            # Take an action in the game.
            # Take an action in the game.
            state, reward, done, _ = self.take_action(state, action)

            # Check if the game is over.
            self.is_done = done

        # When the game is over, render the final game state to the screen.
        self.render(screen, environment, gnome)


def test_game():
    # Create an instance of the Environment class with the specified width, height, and tile size.
    gnome = Gnome(x=0, y=0, environment=None)
    environment = Environment(width=20, height=20, tile_size=32, gnome=gnome)

    # Create an instance of the Gnome class with the specified starting position and the environment object.
    gnome = Gnome(x=10, y=10, environment=environment)

    # Create an instance of the Game class with the environment and gnome objects.
    game = Game(environment=environment, gnome=gnome)

    # Initialize Pygame.
    pygame.init()

    # Set the screen size.
    screen = pygame.display.set_mode((environment.width * environment.tile_size, environment.height * environment.tile_size))

    # Create the game world by generating the tiles.
    # Create the game world.
    environment.create(gnome=gnome)


    # Initialize the clock.
    clock = pygame.time.Clock()

    # Run the game loop.
    while not game.is_done:
        # Get the current state of the environment.
        state = environment.get_state(gnome=gnome)

        # Get the action from the agent.
        action = gnome.act(state, environment)

        # Take a step in the environment.
        state, reward, is_done = environment.step(action, gnome)
        print(action) # print the action

        # Take the action in the environment.
        new_state, reward, done = game.take_action(state, action)

        # Update the game state.
        game.state = new_state
        game.reward = reward
        game.is_done = done

        # Render the environment.
        game.render(screen=screen, environment=environment, gnome=gnome)

        # Update the screen.
        pygame.display.update()

        # Wait for 1/30th of a second.
        clock.tick(30)

    # Close the window.
    pygame.quit()




def main():
    width = 10
    height = 10
    tile_size = 32

    # Create an empty environment array.
    gnome = Gnome(0, 0, None)
    environment = Environment(width, height, tile_size, gnome)

    # Re-assign the environment to the gnome.
    gnome.environment = environment

    # Create a new Game object and pass in the environment and gnome objects.
    game = Game(environment, gnome)

    # Reset the game state.
    game.reset()  # reset the game state (environment and gnome)

    # Defining the screen
    pygame.init()
    screen = pygame.display.set_mode((width * tile_size, height * tile_size))

    # Set the title of the window.
    pygame.display.set_caption("GnomansLand")

    reward = 0  # reward for the current state
    done = False  # boolean to check if the game is over
    action = 0  # action to take in the current state
    state = environment.get_state_space(environment.get_state())  # get the current state of the environment

    while True:
        # Get the current state of the environment.
        state = environment.get_state()

        # Get a list of valid actions in the current state.
        actions = environment.get_valid_actions(state)

        # Choose an action randomly from the list of valid actions.
        action = random.choice(actions)

        # Take the action in the environment.
        new_state, reward, is_done, _ = environment.step(action)

        # Check if the game is over.
        if is_done:
            break

        # Update the current state to the new state.
        state = new_state

        # Render the game state to the screen.
        game.render(screen, environment, gnome)

        # Sleep for a short time to slow down the game.
        time.sleep(1)

    # Run the game loop. This loop will run until the user exits the game.
    # game.run(screen, environment, gnome, action)


# Run the main function.
if __name__ == "__main__":
    # main()
    test_game()