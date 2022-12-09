import pygame
import numpy as np
import sys
# import clock


# Initialize PyGame
pygame.init()

# Set screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Set grid dimensions
GRID_WIDTH = 10
GRID_HEIGHT = 10

# Set tile size
TILE_SIZE = 40

#* Agent Characteristics

class Creature:
    def init(self, x, y):
        self.x = x
        self.y = y
        self.speed = 1
        self.hunger = 0
        self.thirst = 0
        self.sleeping = False # is the creature sleeping?
        self.is_dead = False # is the creature dead?
        # the creature is dark blue when it is awake
        self.color = (0, 0, 128) # the color of the creature (dark blue)
    def move(self, dx, dy):
        """
        move the creature by dx and dy units

        One thing you might want to consider is changing the way you set the creature's x and y positions in the move method. Right now, you are using the max and min functions to constrain the creature's movement to the bounds of the environment. However, this can cause problems if the creature's speed is greater than 1, because it can cause the creature to move outside of the environment.

        One way to fix this is to use the min and max functions to constrain the creature's movement to the bounds of the environment, but also to subtract the creature's speed from the change in x or y if the creature is about to move outside of the environment. This will ensure that the creature always stays within the bounds of the environment, regardless of its speed.

        :param dx: the change in x.
        :type dx: _type_
        :param dy: the change in y.
        :type dy: _type_
        """
        # Constrain movement to the bounds of the environment
        dx = max(0, min(dx, GRID_WIDTH - self.x - 1))
        dy = max(0, min(dy, GRID_HEIGHT - self.y - 1))

        # Subtract speed from change in x or y if necessary
        if self.x + dx * self.speed >= GRID_WIDTH:
            dx -= self.speed
        if self.y + dy * self.speed >= GRID_HEIGHT:
            dy -= self.speed

        self.x += dx * self.speed
        self.y += dy * self.speed


    def eat(self, food):
        if food > 0:
            self.hunger = max(0, self.hunger - food)
        else:
            self.hunger += 1

    def sleep(self, duration):
        if duration > 0:
            self.sleeping = True
        else:
            self.sleeping = False

    def drink(self, water):
        if water > 0:
            self.thirst = max(0, self.thirst - water)
        else:
            self.thirst += 1

    def update(self):
        # Move in a random direction if not sleeping
        if not self.sleeping:
            dx = np.random.choice([-1, 0, 1])
            dy = np.random.choice([-1, 0, 1])
            self.move(dx, dy)

        # Increase hunger and thirst levels over time (1 if awake, 0.5 if sleeping)
        if self.sleeping:
            self.hunger += 0.5
            self.thirst += 0.5
            # set the creature's color to light blue if it is sleeping
            self.color = (0, 0, 255)
        else:
            self.hunger += 1
            self.thirst += 1

        # if the creature is sleeping, it will wake up after a random number of update cycles between 1 and 10 where an update cycle takes 1 second.
        if self.sleeping:
            #note: this is not truely a random number of update cycles, but it is close enough for our purposes I think.
            if np.random.randint(1, 10) == 1:
                self.sleeping = False
                self.color = (0, 0, 128)

        # Check if creature is dead
        if self.hunger >= 100 or self.thirst >= 100:
            self.is_dead = True
        else:
            pass


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

# create the creature
creature = Creature()

# create the food
food = Food()

# create the water
water = Water()

# create the tree
tree = Tree()

# create the list of resources
resources = [food, water, tree]

# create the list of creatures
creatures = [creature]

# create the list of all the objects
objects = [creature, food, water, tree]

# create the list of all the objects that are not the creature
objects_not_creature = [food, water, tree]

# game loop
while True:
    # check for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # draw the background
    screen.fill((255, 255, 255))

    # draw the environment
    for x in range(GRID_WIDTH):
        for y in range(GRID_HEIGHT):
            # draw the grass
            pygame.draw.rect(screen, (0, 255, 0), (x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE))

    # draw the resources
    for resource in resources:
        pygame.draw.rect(screen, resource.color, (resource.x * TILE_SIZE, resource.y * TILE_SIZE, TILE_SIZE, TILE_SIZE))

    # draw the creatures
    for creature in creatures:
        pygame.draw.rect(screen, creature.color, (creature.x * TILE_SIZE, creature.y * TILE_SIZE, TILE_SIZE, TILE_SIZE))

    # update the screen
    pygame.display.update()

    # update the creature
    creature.update()

    # update the resources
    for resource in resources:
        if resource.x == creature.x and resource.y == creature.y:
            if resource == food:
                creature.eat(10)
                resource.is_eaten = True
            elif resource == water:
                creature.drink(10)
                resource.is_drunk = True
            elif resource == tree:
                creature.sleep(10)
                resource.is_eaten = True

    # remove the resources that have been eaten or drunk
    for resource in resources:
        if resource.is_eaten or resource.is_drunk:
            resources.remove(resource)

    # create new resources
    if len(resources) < 3:
        new_resource = np.random.choice(objects_not_creature)
        new_resource.x = np.random.randint(0, GRID_WIDTH)
        new_resource.y = np.random.randint(0, GRID_HEIGHT)
        resources.append(new_resource)

    # check if the creature is dead
    if creature.is_dead:
        creatures.remove(creature)
        # end the game if there are no more creatures
        if len(creatures) == 0:
            pygame.quit()
            sys.exit()

    # update the clock
    clock.tick(1)






# Create game screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Create environment rect
env_rect = pygame.Rect(0, 0, GRID_WIDTH * TILE_SIZE, GRID_HEIGHT * TILE_SIZE)

# Define probabilities for each tile type
tile_probs = {
"grass": 0.8,
"water": 0.1,
"tree": 0.1
}

# Check that tile probabilities sum to 1
assert abs(sum(tile_probs.values()) - 1.0) < 1e-6, "Tile probabilities must sum to 1"

# Define colors for each tile type
tile_colors = {
"grass": pygame.Color("green"),
"water": pygame.Color("blue"),
"tree": pygame.Color("brown")
}


# To change the code from using random tile generation to using a 2D tile array, you can replace the code that generates the tiles in the game loop with code that reads the tiles from the array. Here is an example of how you might do this:

# Create 2D array to store tiles
tiles = np.zeros((GRID_WIDTH, GRID_HEIGHT), dtype=np.int8)

# Populate array with random tile values
for y in range(GRID_HEIGHT):
    for x in range(GRID_WIDTH):
        # Choose tile type based on probabilities
        tile_type = np.random.choice(list(tile_probs.keys()), p=list(tile_probs.values()))

        # Set tile value in array
        tiles[x, y] = tile_type




# Create game loop
running = True
while running:
    # Process events
    for event in pygame.event.get():
        # Check for quit event
        if event.type == pygame.QUIT:
            running = False

    # Clear screen
    screen.fill((0, 0, 0))

    # Draw environment
    for y in range(GRID_HEIGHT):
        for x in range(GRID_WIDTH):
            # Get tile type from array
            tile_type = tiles[x, y]

            # Get tile color
            color = tile_colors[tile_type]

            # Create tile rect
            tile_rect = pygame.Rect(x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE)

            # Draw tile
            pygame.draw.rect(screen, color, tile_rect)

    # Scale screen to create isometric perspective
    screen = pygame.transform.scale(screen, (int(SCREEN_WIDTH * 0.5), int(SCREEN_HEIGHT * 0.5)))

    # Draw environment
    screen.blit(screen, (0, 0))

    # Update display
    pygame.display.flip()