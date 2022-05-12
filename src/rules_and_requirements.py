Abstract:
This article details the rules/actions and variables (methods and attributes) of a character named "The Agent" that spawns into the digital world in a small clearing surrounded by wilderness. The world space consists of tiles that can be one of several options: a forest, a lake, grass land, rocky dirt, and mountains. The Agent learns about his environment through Q-Learning, which is a kind of reinforcement learning. This determines his reactions to stimuli. The agent has one primary goal which is to survive and three secondary goals: Maximize health, minimize distance from points of danger, and occasionally take selfish "greedy" actions while exploring and learn from their outcomes. The Agent must learn from its mistakes how to avoid dangers. He can also identify and save point of interests in the observation space, collect resources from tiles, and carry them in a backpack with limited storage. He begins every day (represented by an epoch) at his cave. He would ideally be able to build tools and progress in technology using raw resources in the environment. He will learn to grow plants and hunt animals. The point is to learn as much as possible through reinforcements, so that The Agent stays alive in this semi-markovian environment.

Methods:
Creation of the Observation Space
The observation space is the environment represented by a 100 x 100 square of semi-random tiles distributed into biomes.
The initial objects, point of interests, or features of the environment are:
- A cave for the agent to live in.
- Three tiles that chain together one edge to create the representation of a lake full of fresh water.
- One tile with a patch of clean dirt that is adjacent to the tile containing the cave. This tile is where the Agent will find food growing that it can eat.
The reinforcement learning algorithm is designed to allow The Agent to reward himself with, or be rewarded by, good actions in this two dimensional world. These rewards will be manifested by the Agent as it finds new ways to modify his environment and save/identify new resources, objects, and materials.
Each time the agent moves it will be assumed that the agent has taken one minute per move. In this way we can say that the agent spends "minutes" while referring to movements.

Attributes for the Agent Class
These innate characteristics of the agent which it is born with that will influence its decisions across epochs.
1. Bravery/Interest - How brave is our agent? Will it be more likely to pursue goals even when it is hungry? This is likely determined by its Risk Value (epsilon) in the Q-learning equation where it considers the "quality of life" that it observes at every moment "t".
2. Past Knowledge-base - What has the agent already learned?
3. Agent Health ( will not span multiple lifespans ).
4. Confidence - how confident is the agent each time it makes a new choice?
5. Speed - Agents begin the game with a speed value of 10 tiles per minute. This means that an agent can traverse a single tile in one "minute" or move if that tile has a speed cost of 10. The cost of each tile is determined by its type and can be found in the tiles dictionary. Agents can level up their speed by increasing the number of times that they repeat the same path (gaining experience). An agent's speed through a tile "n" is equal to the current speed attribute of the agent + 0.5 * (the number of times this agent has been on this exact tile in its lifetime).

Reward Values
The provided list below of reward values will follow the pattern: [point value: action taken].
There are four primary kinds of rewards corresponding to the four primary innate values that the agent cares about: health, interest, speed, and confidence.
+1 health and +1 confidence -0.10 speed: gathered a food item.
+1 health and +1 confidence +1.5 Interest: waited for one minute in safety.
+1 health -1 speed +1 confidence: gathered one bucket of water.
+2 Interest, -1 Confidence, -1 Interest, +1 Speed: identified a point of danger.
+3 Confidence +1 Interest: identified a point of interest to be used in future epochs.
+3 Interest, +1 Confidence, +1 Speed: killed something and harvested its meat which it will need to carry back to the cave eventually. This lowers the agent's speed.
+4 health, +1 Confidence : Carried one bucket of water from the tile with the fresh water lake to the tile with the cave.
+6 health, +1 confidence, +1 speed: killed a creature and harvested its meat which it will need to carry back to the cave. This lowers the agent's speed.

Punishment Values
-0.5 health, -0.25 interest, -0.25 confidence, -0.025 speed: spent one minute exploring.
For every minute that the agent explores it loses half a point of health. This incentives the agent to refresh itself back at its home base. It also loses interest in exploration and confidence as it goes further from home. The speed it can travel decreases by a factor of 0.025 as well which indicates fatigue. NOTE: for future implementation the agent could rest and regain this. Also, the interest and confidence should be relative to the distance the agent is from home or a known point of interest.
-0.25 health, -0.25 interest, -0.25 confidence, -0.025 speed : spent 1 minute traveling within already "discovered" tiles.
-0.5 health, +1 interest, -0.5 confidence, -0.05 speed: spent 1 minute exposed to the wild side of the tile-map which includes lakes, mountains, forests and grassland, rocky dirt ,and wild animals.
-1 health, -1 confidence, +0.10 speed: consumed food when health is full (when Health = 100).
-100 health, -5 confidence, -5 Interest: was killed by a wild animal.

Initialization Actions
The following actions are the "initialization" actions that are taken when the agent is spawned in his new world. If the agent finds a source of food or water for the first time (a new source) then it gathers that food or drinks that water into its backpack and returns to its cave.

Rules of the Simulation
1. Every time The Agent returns to the cave they save the contents of their backpack by depositing the items into an inventory that is accessible so long as the agent remains alive.
2. If the agent dies then the inventory in the cave is cleared and the tiles are rearranged.
3. The agent must remain interested to keep exploring. If their interest attribute falls below 0 then they turn around and begin heading back to the cave.
4. The agent must remain confident to keep exploring. If their confidence attribute falls below the threshold for their personality (this ranges depending on the instantiated agent) then they turn around and begin heading back to the cave.
5. The agent must remain alive and be able to get back to the cave. If their speed attribute * movement cost to return home then they have to make a decision to keep exploring (greedy) or turn and try again the next day. This decision occurs when speed * movement cost = cost to return to home.
6. The agent can use it's speed to gather and save food items that have been stored in their backpack. The food items have a speed cost associated with them. For every consumable item in the agent's backpack that agent's movement is reduced by 0.10 (for a food item) and by 1 (if a pail of water).
In a future implementation of this program the behavior could be changed to be a more complex AI by allowing the agent to have an energy value that is spent with each decision he makes. It should display when it is hungry and needs to hunt, gather or find water. The agent would also have to display some form of exhaustion or boredom that would change its behavior if left on it's own without any way to spend its energy.
Agent Bravery
This is a function of the current health, distance from danger, and the amount of resources it has collected (if any).

Dangers in the Agent's Observation Space
1. Wild animals - If an agent encounters a wild animal as it passes through a tile then it triggers a "wild animal interaction" event which is defined in the events section.
2. Cliffs - If an agent traverses a tile with a cliff (mountain tiles) then there is a thirty percent chance that they will trigger a "natural hazard" event as defined in the events section.

Events
1. Wild Animal Interaction Event -
Resolution of Event: Two variables are assigned, one representing the attack hit points of a wild animal (ranging from 0 to 10) and the other representing the defending points of the agent: dfp =  (random number from 1 to 5)*agent_confidence + agent_speed.
If the Agent wins then they collect 1 food from the dead animal, get +2 confidence, and keep going.
2. Natural Hazard Event -
Resolution of Event: The agent will sustain damage from exposure to the elements. This is a function of the agent's current health and exposure time. New Health of Agent (representing the net damage) = (random_number from 0 to 2)*(interest attribute of the agent)//(backpack item count).

Definition of the Agent's Methods:
The agent consists of a reinforcement learning algorithm which defines the rules and bounds (the methods) of his feedback to his actions. The purpose of the agent is to reinforce good actions and learn from bad ones with positive or negative reinforcements. It is written in the programming language python and its code is available in this document.
The following are the elements used to define the agent's method:
- The environment is composed of two functions: "getter" and "setter".
- A setter is a method that modifies the environment by adding an object or a feature to it.
The project source code is available for download in the attached document.
The agent is implemented as a reinforcement learning algorithm with a set of rules and bounds that it has to follow in order to stay alive and explore its world. The following image displays a flow chart of the reinforcement learning process implemented to control the agent.

Agent Reinforcement Learning Methods:
The following are the methods that are used to weight and reinforce the good or bad actions of the agent within its environment:
1. Harvest - if the agent finds food on a tile that it previously planted seeds on and gathers 1 food.
2. Gather - If it enters an open tile then it gathers the resources in that tile into its backpack: food, gravel, rocks, sticks and grass.
3. Eat - The agent eats a food item from its backpack.
4. Drink - The agent drinks a water item from its backpack.
5. Wait - The agent stands still for 1 minute.
6. Explore - The agent takes steps at it's current speed and checks for a new source of resources (food, water, or rocks) or unexplored tiles and if none are found it will return to its cave per the rules of exploration.

The python code below was written by authors for Towards Data Science as an example of how to implement a simple Reinforcement Learning Approach. This will be adapted to a Q-Learning RL Algorithm and our situation with the agent.

Towards Data Science Code:
import numpy as np

# global variables
BOARD_ROWS = 100
BOARD_COLS = 100
WIN_STATE = (27, 26)
LOSE_STATE = (27, 25)
START = (0, 0)
DETERMINISTIC = True


class State:
    def __init__(self, state=START):
        self.board = np.zeros([BOARD_ROWS, BOARD_COLS])
        self.board[1, 1] = -1
        self.state = state
        self.isEnd = False
        self.determine = DETERMINISTIC

    def giveReward(self):
        if self.state == WIN_STATE:
            return 1
        elif self.state == LOSE_STATE:
            return -1
        else:
            return 0

    def isEndFunc(self):
        if (self.state == WIN_STATE) or (self.state == LOSE_STATE):
            self.isEnd = True

    def nxtPosition(self, action):
        """
        action: up, down, left, right
        -------------
        0 | 1 | 2| 3|
        1 |
        2 |
        return next position
        """
        if self.determine:
            if action == "up":
                nxtState = (self.state[0] - 1, self.state[1])
            elif action == "down":
                nxtState = (self.state[0] + 1, self.state[1])
            elif action == "left":
                nxtState = (self.state[0], self.state[1] - 1)
            else:
                nxtState = (self.state[0], self.state[1] + 1)
            # if next state legal
            if (nxtState[0] >= 0) and (nxtState[0] <= (BOARD_ROWS -1)):
                if (nxtState[1] >= 0) and (nxtState[1] <= (BOARD_COLS -1)):
                    if nxtState != (1, 1):
                        return nxtState
            return self.state

    def showBoard(self):
        self.board[self.state] = 1
        for i in range(0, BOARD_ROWS):
            print('-----------------')
            out = '| '
            for j in range(0, BOARD_COLS):
                if self.board[i, j] == 1:
                    token = '*'
                if self.board[i, j] == -1:
                    token = 'z'
                if self.board[i, j] == 0:
                    token = '0'
                out += token + ' | '
            print(out)
        print('-----------------')


# Agent of player
class Agent:

    def __init__(self):
        self.states = []
        self.actions = ["up", "down", "left", "right"]
        self.State = State()
        self.lr = 0.2
        self.exp_rate = 0.3

        # initial state reward
        self.state_values = {}
        for i in range(BOARD_ROWS):
            for j in range(BOARD_COLS):
                self.state_values[(i, j)] = 0  # set initial value to 0

    def chooseAction(self):
        # choose action with most expected value
        mx_nxt_reward = 0
        action = ""

        if np.random.uniform(0, 1) <= self.exp_rate:
            action = np.random.choice(self.actions)
        else:
            # greedy action
            for a in self.actions:
                # if the action is deterministic
                nxt_reward = self.state_values[self.State.nxtPosition(a)]
                if nxt_reward >= mx_nxt_reward:
                    action = a
                    mx_nxt_reward = nxt_reward
        return action

    def takeAction(self, action):
        position = self.State.nxtPosition(action)
        return State(state=position)

    def reset(self):
        self.states = []
        self.State = State()

    def play(self, rounds=10):
        i = 0
        while i < rounds:
            # to the end of game back propagate reward
            if self.State.isEnd:
                # back propagate
                reward = self.State.giveReward()
                # explicitly assign end state to reward values
                self.state_values[self.State.state] = reward  # this is optional
                print("Game End Reward", reward)
                for s in reversed(self.states):
                    reward = self.state_values[s] + self.lr * (reward - self.state_values[s])
                    self.state_values[s] = round(reward, 3)
                self.reset()
                i += 1
            else:
                action = self.chooseAction()
                # append trace
                self.states.append(self.State.nxtPosition(action))
                print("current position {} action {}".format(self.State.state, action))
                # by taking the action, it reaches the next state
                self.State = self.takeAction(action)
                # mark is end
                self.State.isEndFunc()
                print("nxt state", self.State.state)
                print("---------------------")

    def showValues(self):
        for i in range(0, BOARD_ROWS):
            print('----------------------------------')
            out = '| '
            for j in range(0, BOARD_COLS):
                out += str(self.state_values[(i, j)]).ljust(6) + ' | '
            print(out)
        print('----------------------------------')


if __name__ == "__main__":
    ag = Agent()
    ag.play(50)
    print(ag.showValues())




'''Future Work
There is a chance that the agent will forget where it has been and will get "lost". This occurs when the agent's confidence attribute falls below its personality threshold during exploration and a variable "chance" (which ranges from 0 to 1) is greater than 0.95. In this case the agent begins randomly walking from its current position and loses more health than usual. This is not implemented in the base simulation but in a more advanced version.'''
