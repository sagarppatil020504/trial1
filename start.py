import pygame,sys,time
from modes import *

pygame.init

startscreen=pygame.image.load('').convert.alpha()

#start and quit button

start_font = pygame.font.Font('times new roman',75)
start_but= start_font.render('START',False,'White')
start_rect= start_but.get_rect(center = (ga_w/2,ga_h/2))

quit_font = pygame.font.Font('times new roman',75)
quit_but= quit_font.render('START',False,'White')
quit_rect= quit_but.get_rect(center = ((ga_w/2)+50,ga_h/2))

#when the mouse is pressed on the start rect it should initiate the game

while True:
    if  