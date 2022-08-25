import pygame.sys
from pygame.locals*import
pygame.init()
FPS=30
fps Clock=pygame.time.Clock()

#displaying window for game space
DISPLAY SURFACE= pygame.display.set_mode((40,300)0,32)
Caption=pygame.display.set_caption('Animation')
color=WHITE(255,255,255)

#displaying cat image and coordinates
cat=pygame.image.load('cat.png')
cat x=10
cat y=20

WHILE True;
    if direction='right':
        cat x +=5
      
    if cat y =280
        direction='down'

    if direction='down'
        cat y+= 5
    if cat y +=280
        direction='left'
    elif direction='left':
        cat x-= 5
    if cat x==10
        direction ='up'
    if direction ='up'
        cat y-=5
    if cat y == 10
        direction = 'right'

