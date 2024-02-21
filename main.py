import sys,time,random,pygame
from modes import *
from start import *

pygame.init()

while True:
    for event in pygame.event.get():
        if event type=pygame.Quit:
            pygame.quit()
            sys.exit()
            time.sleep(1)
        stsrt




    screensize.blit('bgimg',(ga_w,ga_h))
    screensize.blit('player1',(ga_w,ga_h))
    screensize.blit('bullet',(ga_w,ga_h))
    screensize.blit('text',(ga_w/5,ga_h/2))
    screensize.blit('start_but',(ga_w/2,ga_h/2))




pygame.display.update()
Clock.tick(60)