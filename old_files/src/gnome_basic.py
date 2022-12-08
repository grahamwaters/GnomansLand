'''
Doc string
'''

demo_variable_imported_from_module: str = "Hello! I come from the module 'module_example.py'"

gnome_name: str = "Jerome"
class Agent:
    voice = "Hey... I'm Greg..." # an example of something the agent could say.
    health = 100 # setting their initial health to 100.
    mood = 0 # the agent has absolutely no mood at all when they are born.
    interest = 0 # starts with no interest at all in features within his/her/their action space.
    strength = 50 # ranges from 1 to 100 and will change based on interactions with environment.
    agent_name = "Greg" # the name of the agent (will change)
    xlocation = 2 # ranges
    # call gamearea len(gamearea)//2 gives the central point if it is an odd number of cols or rows
    ylocation = 2 # ranges
    DistanceFromHome = 0 # the distance between agent and start location

    # ---------------------------------------------------------------------------- #
    #                              constructor method                              #
    # ---------------------------------------------------------------------------- #

    def __init__(self,agent_name, voice):
        """
        summary: initializes the class with the given agent name and voice

        Args:
            agent_name ([type]): [description]
            voice ([type]): [description]
        """
        self.agent_name = agent_name
        self.voice = voice

    # ---------------------------------------------------------------------------- #
    #                                 Gets and Sets                                #
    # ---------------------------------------------------------------------------- #
    #                               voice for speaking                             #
    # ---------------------------------------------------------------------------- #
    def getVoice(self):
        return self.voice
    def setVoice(self, newVoice):
        self.voice = newVoice

    # ---------------------------------------------------------------------------- #
    #                                   strength                                   #
    # ---------------------------------------------------------------------------- #
    def getStrength(self):
        return self.Strength
    def setStrength(self, newStrength):
        self.strength = newStrength
    # ---------------------------------------------------------------------------- #
    #                                     mood                                     #
    # ---------------------------------------------------------------------------- #
    def getMood(self):
        return self.mood
    def setMood(self, newMood):
        self.mood = newMood
    # ---------------------------------------------------------------------------- #
    #                               Movement Speed                                 #
    # ---------------------------------------------------------------------------- #
    def getSpeed(self):
        return self.Speed
    def setSpeed(self, newSpeed):
        # Initialize
        self.speed = newSpeed

    #mood
    #x,y location
    #getting x,y coordinate
    def getXlocationAgent(self):
        return self.xlocation # init

    def getYlocationAgent(self):
        return self.ylocation # init

    # ---------------------------------------------------------------------------- #
    #        Get the interest and set the interest of the agent at runtime         #
    # ---------------------------------------------------------------------------- #
    def getInterest(self):
        return self.interest # init
    def setInterest(self, newInterest):
        self.interest = newInterest

    # ---------------------------------------------------------------------------- #
    #            setting x,y coordinate(s) and location commands                   #
    # ---------------------------------------------------------------------------- #
    def setXlocationAgent(self, newXloc):
        self.xlocation = newXloc #init
    def setYlocationAgent(self, newYloc):
        self.ylocation = newYloc

    #* distance from its home shelter in the space
    def getDistanceFromHome(self):
        return self.DistanceFromHome
    def setDistanceFromHome(self, newDistanceFromHome):
        self.DistanceFromHome = newDistanceFromHome

    #name
    def getName(self):
        return self.agent_name
    def setName(self, newName):
        self.agent_name = newName

    #Methods:
    '''
    talk - asking agent to talk or say something.
    move
    decide # a binary choice about moving
    eat
    later on add drink
    sleep
        turning on
        turning off
    later on add attack
    later on add defend

    '''

    def talk(self):
        #print(self.voice) this is an error
        print(self.getVoice())

    def move(self):
        """
            summary: move the agent through the observation space with actions
            variables:
                x ([type]): [description]
                y ([type]): [description]
                currentX ([type]): [description]
                currentY ([type]): [description]
            Returns:
                (x,y): an x,y coordinate tuple denoting location of the agent within the space.
        """
        # x origin is [2,2]
        x = int(input("Steps in X direction: "))
        y = int(input("Steps in Y direction: "))
        currentX = int(self.getXlocationAgent())
        currentY = int(self.getYlocationAgent())
        print(currentX,",",x)
        self.setXlocationAgent(currentX+x)
        self.setYlocationAgent(currentY+y)

        return x,y
