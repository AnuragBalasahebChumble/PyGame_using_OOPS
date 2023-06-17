# 1. Import Packages
import pygame
import random
import sys
import random
from class_BALL import *

# 2. Define constants
BLACK = (0, 0, 0)
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
FRAMES_PER_SECOND = 30
N_BALLS = 9

# 3. Initialize the world
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

# 4. Load assets: images, sound etc.

# 5. Initialize variables
ballList = []
for oBall in range(0, N_BALLS):
    oBall = BALL(window, WINDOW_WIDTH, WINDOW_HEIGHT)
    ballList.append(oBall)

# 6. Loop Forever
while True:
    # 7. Check for & handle events.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # 8. Do any "per frame" actions
    for oBall in ballList:
        oBall.update()  # tell the ball to update.

    # 9. Clear the window before drawing it again
    window.fill(BLACK)

    # 10. Draw the window element
    for oBall in ballList:
        oBall.draw()   # tell the ball to draw itself.

    # 11. Update the window
    pygame.display.update()

    # 12. Slow down things a bit
    clock.tick(FRAMES_PER_SECOND)
