import pygame,sys,time,random

pygame.init()

ga_w=1000
ga_h=400

screensize=pygame.display.set_mode(ga_w,ga_h)
pygame.display.set_captions('jump if u can')
clock = pygame.time.Clock()

bgimg = pygame.image.load ('').convert_alpha()
player1 =pygame.image.load('').convert_alpha()
bulplant=pygame.image.load('').convert_alpha()
bullet = pygame.image.load('').convert_alpha()

text_font = pygame.font.Font('times new roman',75)
text = text_font.render('WELCOME TO MY GAME',False,'Red')
text_rect=text.get_rect()