"""
    The environment is to be defined/created by tilesets, and preset actions laid out in this file.

"""
import pygame
from sys import exit # closes any code once called


pygame.init() # really important to include before any other code. It initiates all parts.

# todo -- Observation Space should ideally be much more interesting than the one outlined below.
class ObservationSpace:

  Game_Area = [[0,0,0,0,0],
                [0,0,0,0,0],
                [0,0,1,0,0],
                [0,0,0,0,0],
                [0,0,0,0,0]]
  Game_Name = "GnomansLand"

  #Constructor
  def __init__(self,Game_Name):
      """INITIALIZER
      Args:
          Game_Name ([string]): the game name will be supplied by user for now until further changed into survival of the fattest or something witty like that.
      """
      self.Game_Name = Game_Name

  #Get and Set
  def getGame_Area(self):

    return self.Game_Area
  def setGame_Area(self, newGame_Area):
    self.Game_Area = newGame_Area
  # gnome location (new)
  def setGame_Area_Position(self,x, y):
    self.Game_Area[x][y] = 1
  def getGame_Area_Position(self,x, y):
    return self.Game_Area[x][y]

  #TODO method needed: delete previous position,
  def printGame(self):
    for row in self.Game_Area:
      print(row)

# creating a display surface

width = 800
height = 400

screen = pygame.display.set_mode((width,height)) # must be tuple
pygame.display.set_caption("Gnoman's Land")

#frame rate
#maximum frame rate with clock
clock = pygame.time.Clock() # capital c is important here

w = 100
h = 200

#this creates a surface (unattached)
test_surface = pygame.image.load('graphics/background.png')
#!test_surface = pygame.Surface((w,h))

#!test_surface.fill('Red')


while True:

  for event in pygame.event.get(): # gets all possible player input events
    if event.type == pygame.QUIT: # is constant that is 1 when x on window
      pygame.quit() # opposite of pygame.init... once this is run we cannot display anything else anymore
      exit() # will exit the while true loop and not hit line 59

  position = (0,0)
  screen.blit(test_surface,position)

  #will run forever
  #draw elements
  #update everything
  pygame.display.update() # update the surface with any new drawn things
  clock.tick(60) # tells while should not run faster than 60 fps
  # one kind of player input here would be closing the display window
