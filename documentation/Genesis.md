<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/grahamwaters/GnomansLand">
    <img src="../images/logo.png" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">GnomansLand</h3>

  <p align="center">
    A simulation God-Mode Game with free will and reinforcement learning!
    <br />
    <a href="https://github.com/grahamwaters/GnomansLand"><strong>Explore the docs »</strong></a>
    <br />
    <a href="https://github.com/grahamwaters/GnomansLand/issues">Report Bug</a>
    ·
    <a href="https://github.com/grahamwaters/GnomansLand/issues">Request Feature</a>
  </p>
</div>

Feel free to share this repo by Tweeting it!

[![Tweet](https://img.shields.io/twitter/url/http/shields.io.svg?style=social)](https://twitter.com/intent/tweet?text=Get%20over%20170%20free%20design%20blocks%20based%20on%20Bootstrap%204&url=https://froala.com/design-blocks&via=froala&hashtags=bootstrap,design,templates,blocks,developers)

# Outline
## Creators Note
The notes below are compiled over several projects and are disjointed. One important change will be simplifying these and making them performable.

## Abstract and Background:
This document details the rules and bounds (methods and attributes) of a character named The Agent who just woke up in a small clearing surrounded by wilderness, forests, a lake, farm land, and mountains.

The Agent learns about his environment through the use of a reinforcement learning algorithm that programs his reactions to stimuli. The observation space is the environment and the entity lives in a video game where he has to explore the world, and through trial and error, learn how to survive. The Agent has to learn from mistakes and avoid dangers. He can learn waypoints and begins every day at his cave which he is changing into a house with wood from the trees. He learns to build tools and progresses in technology using raw resources in the environment. He will learn to grow plants and keep animals. He can even build a boat with the resources he has. The point is to learn as much as possible through reinforcements, so that The Agent stays alive in this paradise environment.

## Methods:
### Creation of the Observation Space
The observation space is a forest environment with living trees, a lake and mountains at the background. The built objects or features of the environment are:
* The cave (a small shelter in the woods) where the agent begins their life.
* A house (a simple structure made of wood)
* A boat and a motorboat motor.
The reinforcement learning algorithm is designed to allow The Agent to reward himself by using good actions in this natural world; by finding new ways to modify his environment and find new resources, objects, and materials.
* The reward is a value of 1 if The Agent saves the game. If he dies, the reward is 1/2.
* The penalty is an action that diminishes his life, like "falling in the water" or "being burned by lava" which are represented in this game as "drowning" and "burned".
* An action will cause a penalty to The Agent if it leads to his death by drowning or being burned by lava.
* A negative punishment is an action that decreases the life of the agent and is needed when rewarding The Agent for saving his game.
* Training takes place by exploration and experimentation. Random walks are assumed.
* Learning takes place when The Agent has enough information about the environment and he can safely walk from one spot to another.

### Definition of the Agent's Methods:
The agent consists of a reinforcement learning algorithm which defines the rules and bounds (the methods) of his feedback to his actions. The purpose of the agent is to reinforce good actions and learn from bad ones with positive or negative reinforcements. It is written in the programming language python and its code is available in this document.

### The following elements are used to define the agent's method:
* The environment is composed of two functions: "getter" and "setter".
* A setter is a method that modifies the environment by adding an object or a feature to it.
The project source code is available for download in the attached document.

## Results:
The agent will be able to learn from bad actions and move to safer locations and travel new ways that can lead him to places he has never been before. He will modify his environment by building tools and structures as he finds new objects and materials like wood, stone, animals, plants, etc...
The agent will be able to add features to his environment and increase his time in this paradise, as he learns new ways to think as a character and solve problems.
This agent can also learn from good actions and feed the environment with new objects and functions, especially by modifying his waypoints which are measured in distance.
He can learn from mistakes by learning from bad consequences and by avoiding bad consequences in order to stay alive. He can also learn from positive reinforcement and the positive reward of saving his game.
We can add this type of world to a strategy game that requires an intelligent agent to play in an unknown environment and achieve specific objectives, like in Starcraft or Dune.
- Define the observation space
- Define the actions and their rules
- Define the observation methods
- Design the reward function (value) and its bounds (max, min, value). This value is used to reward or punish The Agent's actions.
- Design the penalty function and its bounds. This value is used to punish The Agent's actions.
- Design the bounds of the penalties, if it is greater or lesser than the bounds of the reward, then there is no need for a negative reinforcement.
- Define new features to be added to the world like new objects and materials.
- If The Agent does not need these features, then they will not be added to his environment.
- Design a list of available actions with some default methods
- Run a random walk until The Agent encounters an obstacle in his environment.
Programing Languages: Python 3 was used to implement this project, while using numpy and scipy modules for calculations and execution.

## The Agent Class
The agent class is a class instance that will be used to have the individual methods of each method.
The class is defined in this document with the following methods:
- getter_funcs which defines functions that can be used to get objects or features in an environment.
- setter_funcs which defines functions to modify objects or features in the environment.
- reward_function and its bounds, this is the value that will reward or punish actions taken by the Agent.  This value can be a number, a string, a variable (integer) or even another function. It will be divided into 3 parts: max(reward), min(reward), and value (reward).
- penalty_function, this is the value that will be used to punish actions taken by The Agent.  This value can be a number, a string, a variable (integer) or even another function. It will be divided into 2 parts: max(penalty), min(penalty).
- action_funcs which is used to define methods that are called and return an action. This method needs to have bounds for different parameters such as distance for waypoints or rotation for strategy games.  It may accept objects or features in the environment as parameters and return an action such as "walk left", "walk right", "walk forward", "build a house", etc.
- set_action_funcs which is used to define methods that are called and modify objects or features in the environment. This method needs to have bounds for different parameters such as distance for waypoints or rotation for strategy games. It may accept objects or features in the environment as parameters and modify them such as "set house 2", "set house 1", "build a house", etc.
- at_goal, this function return True if The Agent reaches the coordinates of his destination.

## Explanation of Functions in the Agent Class
The waypoint functions and method names are pretty much self explanatory. The reward function is used to reward decisions made by the agent, essentially giving it a bonus for doing what it was programmed to do. The penalty function is used to give a penalty if the action it took was not what the agent was told to do. The waypoint functions are fairly simple, and only need bounds on different locations in the environment in order for them to be recognized as either a goal or an obstacle. These different parameter types are not going to be implemented because they have no useful purpose.

The set_action_funcs method is probably the most useful part because it allows us to modify the environment in any way we see fit. For now, we are going to leave this function mostly empty except for the setName function that will allow The Agent to tell people his name.

## Getting The Agent to Talk:
Now that we have a basic agent class, it's time for him to "speak" and let people know who he is. Experience tells me that a good place to start is with his mouth. Agents are not very good at talking so we need a pretty simple algorithm for this part of the class. Let's just do it that way.

def getMouth():
The code for this function is pretty much self explanatory:
'''Get the agent's mouth and print it.'''

   def talk(self):
The code for this function is pretty much self explanatory:
'''Say something and print it.'''

   def move(self):
The code for this function is also pretty much self explanatory:

   The code needed to make all of these functions work is contained in a Agent class that implements The Agent's observations and rules, the waypoint functions, the strategy function, etc. We will run through some of these methods in order to understand how they are implemented.

The Agent class is pretty straightforward, as you can see from the code below, with the exception of two methods (remember, we don't implement type inheritance yet):

   def agent_name():
This method has a much simpler problem in that it can return any text string. We will come back to it later for creating The Agent's name when we want to differentiate between different The Agents.

def setName(self,newName):
This method is called to update the agent name. Any legal string of characters will do.

def waypoint(self, xl,xr,yl,yr):
This method is where we tell Agent to implement the waypoint strategy function to get him from one point in space to another. The parameters are the coordinates of that location and a next location in space. We will come back to this method later when we actually need it for our program. For now, we are going to work on The Agent's mouth and getting him talking. We have accomplished this by using a public variable (mouth) and a talk function that prints out what his mouth variable contains. We are going to define it as a simple list at the top of the file for the moment and then make it more complicated after we get some basic stuff working.

The main thing that still remains to be done, however, is to get The Agent moving from one place to another, and talking. Let's do that now. Here is what we need:
As shown in Figure 5-2, we have already implemented move_to_x and move_to_y as waypoint functions so that The Agent will move from one location (waypoint) to another. His mouth is also implemented as a simple list at this point so that he can tell people his name. So we have accomplished much functionality but not all of it yet.


The way that we are going to accomplish this functionality is by creating a new method called get_ready which will check to see if any of his sensors are available and make sure that the first sensor is ready (i.e., not blocked by obstacles) and move The Agent forward when it reports that it is fine. To do this, we need to check whether a sensor has become available. We can accomplish this by calling has_sensor_ready on Agent and passing in the appropriate sensor as an argument. How do we get from one location to another? Obviously, we need a way point function for each location in order for Agent to move from one point of space to another. But we also need a way to make sure that the step count is correct and that the sensor is fine. So we need to make sure that Agent's Speed has not been set too low so that he does not move too fast when he needs more steps for his next move. We can accomplish this by using a new method in our Agent class called check_speed. When we do this, however, our agent will just be moving from one location to another without any speech! To make it work as intended, we need to use a strategy function called get_new_x and get_new_y which will allow The Agent to use the sensors properly so he can actually talk to you instead of moving in place.

def get_sensors():
This method is fairly complicated because it has to check various things like the agent's name, if the agent is ready, and if the sensors are available before it can return an actual sensor. The details of which are shown below:

def getName(self):
We want The Agent to tell people his name when he finds himself not moving for some period of time. In order to make this happen, we will have The Agent execute this strategy function automatically when he finds himself in a new place.

  def get_ready(self):
This new method will return a True or False value depending if The Agent is ready or not to move on based on his available sensors.

## Agent Movement Methods
Now that we have got the information we need to get The Agent moving I'll take you through the methods that we wrote to accomplish this functionality. The code for each method is shown below within square brackets [] and then define the method name before calling it.

def set_speed(self,sz):
This function sets the speed of The Agent at a given step count between 0 (no movement) and 1 (straight ahead). It is defined as a new waypoint function so that when The Agent needs to change his speed he doesn't just move forward at 1 but instead he moves in a waypoint fashion. We can also use it as a way to make him stop when necessary.


def check_speed(self):
This method is called every time we move The Agent. It compares The Agent's Speed to the threshold he has been set. If a problem is found, it tells us and that input stops us from moving forward. We could also use this method to make The Agent move slower when he is not ready to take steps (for the purpose of getting him talking)


def get_new_x(self):
This function returns the new location for The Agent if he needs more steps for his next move or tries to go straight ahead if his speed limit is 0 or 1. This function calculates the new location for The Agent based on the formula given above.


def get_new_y(self):
This function returns the new location for The Agent if he needs more steps for his next move or tries to go straight ahead if his speed limit is 0 or 1. This function calculates the new location for The Agent based on the formula given above.


## Agent Speech Functionality Methods
The methods that we will use to make The Agent actually talk will all be called by some other method which we have yet to create. These methods will be used by the get_new_x and get_new_y functions that we just wrote to call the correct waypoint strategy functions in order to move The Agent forward.

### def say(self,s):
This function is called when The Agent wants to say something. It uses find_sensor to take a look at all the sensors and make sure one is ready before calling it. If a sensor is not ready, it prints out that message instead of calling the strategy function for the waypoint he wants to use. This ensures that The Agent can actually talk instead of move about as he needs more steps before his next movement or needs more space for all his sensors before he can move on.

### def get_new_x(self,s):
This function is used by the say function to execute itself whenever The Agent is ready to move another step. It uses say as an argument and passes in the new location of the agent. If a sensor is available it will check if The Agent needs more steps and give him those if so. Otherwise it will simply print out that this step can go forward for now.

How will our Agent 'learn' from its mistakes and make decisions?
In order to make the agent make decisions, it will have to use a learning function which tells us what has happened in the past. This function will look at the options that have been given to The Agent in the past and determine what could have happened if he had chosen one of those options. If the agent was able to choose an option but did not and simply chose another option - or if he was able to choose an option but chose a different waypoint than expected - then we need some sort of feedback mechanism so that we can give The Agent data so as not to contradict what his brain is expecting him to do. We will accomplish this by using a new method in our Agent class called remember. This method will keep track of all the data that The Agent is given, use a learning algorithm to determine what The Agent should have done, and then remember what would have happened if he had chosen one of the available options. As you can see below:

### def remember(self,s):
This method is not as simple as all that but shows the basic method we will be using to store data and take action based on it. The idea behind this mechanism is that we want The Agent to choose the correct waypoint initially, but if he doesn't, then he will remember what his brain should have done instead. When it comes time for him to choose a next waypoint, we will let The Agent know what would have happened if he had chosen one of the previous wayspottes so that The Agent can choose accordingly.
The Agent uses the remember method with a different set of arguments and returns a Boolean value.
### The arguments are:

    s - an array containing the last few sensor readings
    h - an array containing the most recent history of all the waypoints chosen and their outcomes. This will help The Agent understand that if he chooses a certain waypoint, then he may end up in different locations than he would have expected at first.
    h_t - the history for the tth step. The Agent will compare his input from this step to his memory of his previous steps and make decisions based on how those correlate to what happened before and what should have happened in order to avoid contradiction.
    h_t-1 - the history for the tth step. The Agent will compare his input from this step to his memory of his previous steps and make decisions based on how those correlate to what happened before and what should have happened in order to avoid contradiction.

We want some randomness also so the agent can choose to make a less than optimal decision out of preference.

Innate opinions that will be programmed into the Agent's "brain" and will influence their decision-making and choices.
    1. The Agent does not like to be further than ten blocks from home.
    2. The Agent increases his walking speed as he gets closer to danger and decreases his walking speed as he gets further away from danger.
    3. The Agent does not like to be further than ten blocks from the objective.
    4. The Agent will check its memory to see whether it should perform an action before moving forward.
    5. The Agents memory contains up to 100 epochs only.
    6. The Agent does not like to be closer than two blocks to an enemy.
    7. The Agent does not like being within five blocks of the objective and an enemy at the same time.
    8. If the Agent is within 5 blocks of the objective and there is an enemy, it may choose a different waypoint than what its memory tells it for that step.
    9. The Agent does not like being more than two blocks from any ally if there are enemies nearby.
    10. The Agent does not like being more than two blocks from an enemy, if there are allies nearby.
    11. The Agent does not like to be farther than two blocks from any ally it is close to.
    12. The Agent will always take into account the amount of motion in the past of each waypoint that is part of its memory before choosing which one to choose.
    13 The Agent likes to be within 5 blocks (1/6th radius) of the objective and at least one block away from a group of enemies and 5 blocks away from an ally that is not adjacent to a group of enemies.
    1.  The Agent will check its memory to see if it has less than 100 epochs in its memory.
    2.  If the Agent is more than 10 blocks away from the objective and there are no enemies around, he may choose any waypoint (but will have to answer for this decision at the end of the epoch).

        A quick note about #2/#3/4: The Agent's speed is determined by how far it is from danger, so that when he is close to danger he feels scared and tries to get away quickly, and when he is far from danger he is relaxes and moves at a normal pace. The Agent also speeds up when trying to get back home...

    3.  At the point of its birth, the agent will be assigned one of the following personality types:
        type 1: Eager: The agent has higher speed and less awareness of dangers but gathers 1.5 x as much as the other types do in resources.
        type 2: Cautious: The agent has lower speed, but is 2.0x more aware of dangers (can see two times as far away).
        type 3: Inventive: The agent has normal speed, and awareness of dangers but can create and craft 2.0x faster than the other personalities.
        type 4: Resourceful: The agent has 1.5x speed and can gather 1.5x more resources than the other personalities.




"TEra One": The primary story we will be crafting around this agent is one of survival in a grid world space that has resources, nights and days, and enemies.
    1. Spawns The Agent with no weapons.
    2. The agent starts with 100 health and loses one health per day.
    3. The agent has 100 hit points which are reduced every time they encounter a danger/enemy on their path. 4. During the day, the agent moves at a speed of 1.7 blocks/second, with a difficulty to change this value being an easy modification to The Agent's class.
    5. The agent is only able to see about 2 blocks ahead of him, 1 block to his left and right and approximately one block behind him (NOTE: these values are subject to change as we refine our idea).
    6. The Agent starts in the center of a square 21x21 block grid world that contains a small lake, a cave that the agent lives in, a forest of trees and several fields.
    7. The agent's objective is to survive on this grid, by gathering, eating and sleeping. The agent will take one of two paths when it begins: a path that goes through the mountains to the lake or a path that goes through the forest. The agent has the choice of which path it will take as its memory will aid it in determining which route it starts with.
    8. The Agent can choose ANY waypoint (must be part of its memory) to begin at and go through when it spawns in.



    # notes from AI about PyBrain -- look into this for potential use
PyBrain is an open source library that allows you to build agents that are capable of learning and classifying data, and making decisions based on it. PyBrain does not require that you know how the brain works in order to use it, all you have to do is write your code so as to allow The Agent to learn what would have happened if he had chosen a different action than the one he took. Since it is open source, PyBrain can be improved upon and extended by anyone, so the research team at The University of Washington's Machine Learning Group would like to hear from anyone interesting in helping us figure out how our brains work or what they look like inside. You can find more information at http://brain.csail.mit.edu/.



The Agent's actions are controlled by the controller, who also determines its current position. It also supposes that the current position of the agent can change over time by using an algorithm (and learning) called Markov Decision Processes (MDP). The agent can also learn from its experiences and modify its knowledge base to make better decisions in the future. If the agent wants to find a new target, it will send a request to the controller with a set of information
The controller (or supervisor) would then respond by sending one or more messages that govern how the Agent should perform an action. The process is repeated until the agent reaches his goal. Here is a description of how this might look:
In order for the agent to receive feedback, it has to be able to communicate with its supervisor (or controller). It did so by sending requests and receiving responses in order to determine if it was in a safe environment and/or if any obstacles were in its way. This can be accomplished by sending messages over the network. The network also allows for communication between two agents if they are in close proximity to each other (such as two agents moving towards the same goal at different rates).

One of the reasons The Agent was able to learn from its environment is that it had a map stored in its memory. It was given this map after it was created or "unboxed" in order to give it a head start on what it should expect and what it could do in its environment. However, if this map were lost, the agent would have no way of knowing where things might be or how far away they might be. The robot's memory also stores his path (i.e. actions taken) while moving in its environment. The Agent also has a database of information (knowledge base) stored in his memory that it uses to make decisions.

PyBrain is an open source software package that implements various machine learning algorithms and neural networks. The research team at the University of Washington used PyBrain to develop an agent capable of learning from its environment, making decisions based on what it knows about that environment, and classifying information about it; such as recognizing the difference between a red ball and a green one.

Abstract and Background:
This article details the rules and bounds (methods and attributes) of a character named The Agent who just woke up in a small clearing surrounded by wilderness, forests, a lake, farm land, and mountains. The Agent learns about his environment through the use of a reinforcement learning algorithm that programs his reactions to stimuli. The observation space is the environment and the entity lives in a video game where he has to explore the world, and through trial and error, learn how to survive. The Agent has to learn from mistakes and avoid dangers. He can learn way points and begins every day at his cave which he is changing into a house with wood from the trees. He learns to build tools and progresses in technology using raw resources in the environment. He will learn to grow plants and keep animals. He can even build a boat with the resources he has. The point is to learn as much as possible through reinforcements, so that The Agent stays alive in this paradise environment. The reinforcement learning algorithm is designed to allow The Agent to reward himself by using good actions in this natural world; by finding new ways to modify his environment and find new resources, objects, and materials.
