import pygame
import sys
pygame.init()
WIDTH,HEIGHT=800,800
screen=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("DDA Algorithm")
white=(225,255,255)
black=(0,0,0)


def dda_line_draw(x1,y1,x2,y2):
    dx=(x2-x1)
    dy=(y2-y1)
    if (abs(dx)>abs(dy)):
        step=abs(dx)
    else:
        step=abs(dy)

    xinc=dx/step
    yinc=dy/step

    x=x1
    y=y1

    for i in range(step):
        
        x=x+xinc
        y=y+yinc
        screen.set_at((round(x),round(y)),white)
    
                   

while True:
    for event in pygame.event.get():
        if event.type==pygame.quit:
            pygame.quit()
            sys.exit()
    screen.fill(black)

    dda_line_draw(50,150,100,100)
    dda_line_draw(100,100,150,150)
    dda_line_draw(150,150,50,150)
    dda_line_draw(50,150,50,300)
    dda_line_draw(50,300,150,300)
    dda_line_draw(150,300,150,150)
    dda_line_draw(75,300,75,250)
    dda_line_draw(75,250,125,250)
    dda_line_draw(125,250,125,300)
    pygame.display.flip()


