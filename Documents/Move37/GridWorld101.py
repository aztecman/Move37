import pygame, sys
from pygame.locals import *

# TODO: document the code
# TODO: add an introductory paragraph explaining the premis ie:
# For simplicity of explanation we are starting with a optimal policy for each state
# OR
# For simplicity our Agent will trace back from the terminal state

# TODO: post code to GITHUB
# TODO: add a setValue function to the cell object
# TODO: add a "value = _" label to each cell within the drawCell function
# TODO: create a icon for the agent, such as a label that says 'agent'
# TODO: code the agent moving around with a 20% chance of slipping

GREEN =  (0, 204, 0)
WHITE = (255, 255, 255)
RED = (204, 0, 0)
TILESIZE = 80
TILEOFFSET = 5
BOARDWIDTH = (TILESIZE + TILEOFFSET) * 4 + TILEOFFSET
BOARDHEIGHT = (TILESIZE + TILEOFFSET) * 3 + TILEOFFSET + 40

class Cell:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
        self.reward_state = False
        self.punish_state = False
        self.color = WHITE
             
    def coordinates(self):
        return self.x, self.y
    
    def drawCell(self, x_coord, y_coord):
        x_pixel = coordToPixelSpace(x_coord)
        y_pixel = coordToPixelSpace(y_coord)
        pygame.draw.rect(DISPLAYSURF, self.color, (x_pixel, y_pixel, TILESIZE, TILESIZE))

    def getColor(self):
        return self.color
    
    def setPunish(self):
        self.color = RED
        self.punish_state = True

    def setReward(self):
        self.color = GREEN
        self.reward_state = True
            
def coordToPixelSpace(coord):
    pixelPosition = TILEOFFSET + coord*(TILESIZE + TILEOFFSET)
    return pixelPosition

def terminate():
    pygame.quit()
    sys.exit()
    
def checkForQuit():
    for event in pygame.event.get(QUIT): # get all the QUIT events
        terminate() # terminate if any QUIT events are present
    for event in pygame.event.get(KEYUP): # get all the KEYUP events
        if event.key == K_ESCAPE:
            terminate() # terminate if the KEYUP event was for the Esc key
        pygame.event.post(event) # put the other KEYUP event objects back


        
cell_list = []
for i in range(4):
    for j in range(3):
        cell_list.append(Cell(i, j))

cell_list[9].setReward()
cell_list[10].setPunish()
del cell_list[4]

pygame.init()
DISPLAYSURF = pygame.display.set_mode((BOARDWIDTH, BOARDHEIGHT))

for i in range(len(cell_list)):
    cell_list[i].drawCell(cell_list[i].coordinates()[0], cell_list[i].coordinates()[1])

pygame.display.update()

while True:
    checkForQuit()
