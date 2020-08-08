# Press any key to pause and again for continue playing
# Click on any cell to change status

######### GAME RULES #########
# For a space that is 'populated':
    # Each cell with one or no neighbors dies, as if by solitude.
    # Each cell with four or more neighbors dies, as if by overpopulation.
    # Each cell with two or three neighbors survives.
# For a space that is 'empty' or 'unpopulated'
    # Each cell with three neighbors becomes populated.

import pygame
import sys
import math
import random
from pygame.locals import *

CELL_WIDTH = 10

SIZE = 400, 400
RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (150, 150, 150)

def exist(x,y):
    if(x > 0 and y > 0 and x < SIZE[0] // CELL_WIDTH and y < SIZE[1] // CELL_WIDTH):
        return Grid[x][y].status
    return 0

class Cell(Rect):
    def __init__(self, x, y, status=0):
        self.x = x
        self.y = y
        self.status = status
    
    def draw(self, screen):
        if self.status == 1:
            color = WHITE
        else:
            color = BLACK
        pygame.draw.rect(
            screen,
            color,
            Rect(self.x * CELL_WIDTH, self.y * CELL_WIDTH, self.x + CELL_WIDTH, self.y + CELL_WIDTH)
        )
        
    def count(self, Grid):
        x = self.x
        y = self.y
        sum = 0
        for i in [-1, 0, 1]:
            for j in [-1, 0, 1]:
                if not(i == 0 and j == 0):
                    sum = sum + exist(x + i, y + j)
        return sum
    
    def check(self, Grid):
        count = self.count(Grid)
        if self.status == 1:
            if (count <= 1 or count >= 4):
                self.status = 0
        if self.status == 0 and count == 3:
            self.status = 1

Grid = []

for i in range(0,40):
    a = []
    for j in range(0,40):
        a.append(Cell(i,j, random.randint(0,1)))
    Grid.append(a)

pygame.init()
screen = pygame.display.set_mode(SIZE)
pause = 0
while 1:
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
        if event.type == MOUSEBUTTONUP:
            x = event.pos[0] // CELL_WIDTH
            y = event.pos[1] // CELL_WIDTH
            Grid[x][y].status = 1 - Grid[x][y].status
        #pause on keyboard pressed
        if(event.type == KEYDOWN):
            pause = 1 - pause

    screen.fill(GRAY)

    for line in Grid:
        for cell in line:
            cell.draw(screen)
    if(pause == 0):
        Gridtemp = Grid
        for line in Grid:
            for cell in line:
                cell.check(Gridtemp)
    pygame.time.Clock().tick(10)
    pygame.display.flip()

pygame.quit()