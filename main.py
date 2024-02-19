import sys,time,random,pygame

pygame.init()

ga_w=1000
ga_h=400

screensize=pygame.display.set_mode(ga_w,ga_h)
pygame.display.set_captions('jump if u can')
clock = pygame.time.Clock()

bgimg = pygame.image.load ('').convert_alpha()
player1 =pygame.image.load('').convert_alpha()
player2 = pygame.image.load('').convert_alpha()

text_font = pygame.font.Font('times new roman',75)
text = text_font.render('WELCOME TO MY GAME',False,'Red')
rect(text)





while True:
    for event in pygame.event.get():
        if event type=pygame.Quit:
            pygame.quit()
            sys.exit()
            time.sleep(1)

    screensize.blit('bgimg',(ga_w,ga_h))
    screensize.blit('player1',(ga_w,ga_h))
    screensize.blit('player2',(ga_w,ga_h))
    screensize.blit('text',(ga_w/5,ga_h/2))





pygame.display.update()
Clock.tick(60)