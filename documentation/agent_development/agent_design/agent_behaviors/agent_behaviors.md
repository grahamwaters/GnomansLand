# Agent Attributes

Gnomes have the following attributes in their profiles.

1. A personality
2. A current health score (ranging from 0 (dead) to 100)
3. A skill level in each of the core competencies that gnomes need to have to live within the action space.
    1. Combat - emerges in phase three to four depending on implementation.
    2. Building - emerges in phase two when the gnomes find **Descartes station.**
    3. Farming - emerges in phase three when the population has settled around *Descartes station*
    4. nurturing - emerges in phase three.
    5. foraging - Emerges in phase three
    6. exploration - Emerges in phase three
    7. hunting - Emerges in phase three
4. A name that is randomly generated by the python `faker` package
5. An age (the gnomes live a maximum of 130 years and pass their acquired characteristics at half-value to their offspring. So if a gnome with a farming skill score of 1450 dies leaving two children, their children get + 725 farming XP when their parent passes.
6. An element of randomness that makes the gnome occassionally behave in ways that are against the programming. This is simply to augment the robust nature of the RL Agent Policies, and the environment as well which also is learning from the Gnomes.
7. They have a designation that is either True or False called: `in the order` which represents their position as **in Eve’s Protectorate** or not.
8. Attributes that are trained or innate.
    **Innate**:
    1. **A personal fortune score** - a value from 1 to 100 that determines how likely the gnome is to either win a fight they are in, find a resource, be undetected by enemies while away from the city, or locate a relic while exploring. Starts at a random number from 1 to 100.
    **Trained**:
    1. **Savagry**: How much the gnome favors helping itself over others. Starts at a random number from 1 to 100.
    2. **Teamwork**: How much the gnome favors helping everyone over itself. Starts at a random number from 1 to 100.


# Agent Behaviors

Gnomes have the following behaviors in their profiles. Behaviors are defined as a list of actions that are executed in order. Each action is an instance of the `Action` class. The `Action` class has the following attributes:

1. A `name` - a string that describes the action.
2. A `function` - a function that is executed when the action is called.
3. A `priority` - a number that determines the order in which the actions are executed. The lower the number the higher the priority.
4. A `condition` - a boolean function that determines if the action is executed or not. If the condition is not met the action is skipped.
5. A `probability` - a number from 1 to 100 that determines how likely the action is to be executed. This number is compared to a random number from 1 to 100. If the random number is less than the probability the action is executed. If the random number is greater than the probability the action is skipped.

## Exploration

Exploration is the process by which the gnome looks for new resources in the environment. The gnome will explore the environment until it finds a resource or until it has explored the entire environment. Exploration is a behavior that is defined in the `exploration` function in the `gnome.py` file. The exploration function is called in the `gnome.py` file in the `step` function. The exploration function is defined as follows:

    def exploration(self):
        if self.in_the_order:
            return [Action(name='explore',
                           function=self.explore,
                           priority=1,
                           condition=lambda: self.exploration_skill >= 50,
                           probability=100),
                    Action(name='return to city',
                           function=self.return_to_city,
                           priority=2,
                           condition=lambda: True,
                           probability=100),
                    Action(name='explore',
                           function=self.explore,
                           priority=3,
                           condition=lambda: self.exploration_skill < 50,
                           probability=100),
                    Action(name='return to city',
                           function=self.return_to_city,
                           priority=4,
                           condition=lambda: True,
                           probability=100)]

The exploration function is a list of actions. The first action, `explore`, is called if the gnome has a `exploration_skill` score of 50 or greater. The second action is called if the gnome has a `exploration_skill` score of less than 50. The gnome will explore until it finds a resource

## Farming

Farming is the process by which the gnome looks for new resources in the environment. The gnome will explore the environment until it finds a resource or until it has explored the entire environment. Exploration is a behavior that is defined in the `exploration` function in the `gnome.py` file. The exploration function is called in the `gnome.py` file in the `step` function. The exploration function is defined as follows:

    def farming(self):
        if self.in_the_order:
            return [Action(name='farm',
                           function=self.farm,
                           priority=1,
                           condition=lambda: self.farming_skill >= 50,
                           probability=100),
                    Action(name='return to city',
                           function=self.return_to_city,
                           priority=2,
                           condition=lambda: True,
                           probability=100),
                    Action(name='farm',
                           function=self.farm,
                           priority=3,
                           condition=lambda: self.farming_skill < 50,
                           probability=100),
                    Action(name='return to city',
                           function=self.return_to_city,
                           priority=4,
                           condition=lambda: True,
                           probability=100)]

The exploration function is a list of actions. The first action, `explore`, is called if the gnome has a `exploration_skill` score of 50 or greater. The second action is called if the gnome has a `exploration_skill` score of less than 50. The gnome will explore until it finds a resource

## Building

Building is the process by which the gnome looks for new resources in the environment. The gnome will explore the environment until it finds a resource or until it has explored the entire environment. Exploration is a behavior that is defined in the `exploration` function in the `gnome.py` file. The exploration function is called in the `gnome.py` file in the `step` function. The exploration function is defined as follows:

    def building(self):
        if self.in_the_order:
            return [Action(name='build',
                           function=self.build,
                           priority=1,
                           condition=lambda: self.building_skill >= 50,
                           probability=100),
                    Action(name='return to city',
                           function=self.return_to_city,
                           priority=2,
                           condition=lambda: True,
                           probability=100),
                    Action(name='build',
                           function=self.build,
                           priority=3,
                           condition=lambda: self.building_skill < 50,
                            probability=100),
                    Action(name='return to city', function=self.return_to_city,
                           priority=4,
                           condition=lambda: True,
                           probability=100)]

The exploration function is a list of actions. The first action, `explore`, is called if the gnome has a `exploration_skill` score of 50 or greater. The second action is called if the gnome has a `exploration_skill` score of less than 50. The gnome will explore until it finds a resource

## Hunting

Hunting is the process by which the gnome looks for new resources in the environment. The gnome will explore the environment until it finds a resource or until it has explored the entire environment. Exploration is a behavior that is defined in the `exploration` function in the `gnome.py` file. The exploration function is called in the `gnome.py` file in the `step` function. The exploration function is defined as follows:

    def hunting(self):
        if self.in_the_order:
            return [Action(name='hunt',
                           function=self.hunt,
                           priority=1,
                           condition=lambda: self.hunting_skill >= 50,
                           probability=100),
                    Action(name='return to city',
                           function=self.return_to_city,
                           priority=2,
                           condition=lambda: True,
                           probability=100),
                    Action(name='hunt',
                           function=self.hunt,
                           priority=3,
                           condition=lambda: self.hunting_skill < 50,
                           probability=100),
                    Action(name='return to city',
                           function=self.return_to_city,
                           priority=4,
                           condition=lambda: True,
                           probability=100)]

The exploration function is a list of actions. The first action, `explore`, is called if the gnome has a `exploration_skill` score of 50 or greater. The second action is called if the gnome has a `exploration_skill` score of less than 50. The gnome will explore until it finds a resource

## Gathering

Gathering is the process by which the gnome looks for new resources in the environment. The gnome will explore the environment until it finds a resource or until it has explored the entire environment. Exploration is a behavior that is defined in the `exploration` function in the `gnome.py` file. The exploration function is called in the `gnome.py` file in the `step` function. The exploration function is defined as follows:

    def gathering(self):
        if self.in_the_order:
            return [Action(name='gather',
                           function=self.gather,
                           priority=1,
                           condition=lambda: self.gathering_skill >= 50,
                           probability=100),
                    Action(name='return to city',
                           function=self.return_to_city,
                           priority=2,
                           condition=lambda: True,
                           probability=100),
                    Action(name='gather',
                           function=self.gather,
                           priority=3,
                           condition=lambda: self.gathering_skill < 50,
                           probability=100),
                    Action(name='return to city',
                           function=self.return_to_city,
                           priority=4,
                           condition=lambda: True,
                           probability=100)]


The exploration function is a list of actions. The first action, `explore`, is called if the gnome has a `exploration_skill` score of 50 or greater. The second action is called if the gnome has a `exploration_skill` score of less than 50. The gnome will explore until it finds a resource

## Trading

Trading is the process by which the gnome identifies needs

    def trading(self):
        if self.in_the_order:
            return [Action(name='trade',
                           function=self.trade,
                           priority=1,
                           condition=lambda: self.trading_skill >= 50,
                           probability=100),
                    Action(name='return to city',
                           function=self.return_to_city,
                           priority=2,
                           condition=lambda: True,
                           probability=100),
                    Action(name='trade',
                           function=self.trade,
                           priority=3,
                           condition=lambda: self.trading_skill < 50,
                           probability=100),
                    Action(name='return to city',
                           function=self.return_to_city,
                           priority=4,
                           condition=lambda: True,
                           probability=100)]

The exploration function is a list of actions. The first action, `explore`, is called if the gnome has a `exploration_skill` score of 50 or greater. The second action is called if the gnome has a `exploration_skill` score of less than 50. The gnome will explore until it finds a resource

## Farming

Farming is the process by which the gnome looks for new resources in the environment. The gnome will explore the environment until it finds a resource or until it has explored the entire environment. Exploration is a behavior that is defined in the `exploration` function in the `gnome.py` file. The exploration function is called in the `gnome.py` file in the `step` function. The exploration function is defined as follows:

    def farming(self):
        if self.in_the_order:
            return [Action(name='farm',
                           function=self.farm,
                           priority=1,
                           condition=lambda: self.farming_skill >= 50,
                           probability=100),
                    Action(name='return to city',
                           function=self.return_to_city,
                           priority=2,
                           condition=lambda: True,
                           probability=100),
                    Action(name='farm',
                           function=self.farm,
                           priority=3,
                           condition=lambda: self.farming_skill < 50,
                           probability=100),
                    Action(name='return to city',
                           function=self.return_to_city,
                           priority=4,
                           condition=lambda: True,
                           probability=100)]


The exploration function is a list of actions. The first action, `explore`, is called if the gnome has a `exploration_skill` score of 50 or greater. The second action is called if the gnome has a `exploration_skill` score of less than 50. The gnome will explore until it finds a resource