import pygame
import sys
pygame.init()
WIDTH,HEIGHT=800,800
screen=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("BLA Algorithm")
white=(225,255,255)
black=(0,0,0)


def bla_line_draw(x1,y1,x2,y2):
    dx=abs(x2-x1)
    dy=abs(y2-y1)
    if x2>x1:
        lx=1
    else:
        lx=-1
    if y2>y1:
        ly=1
    else:
        ly=-1
    
    x = x1
    y = y1
    
    if dx>dy:
        p=2*dy-dx
        for i in range(dx):
            if p<0:
                x=x+lx
                y=y
                p=p+2*dy
            else:
                x=x+lx
                y=y+ly
                p=p+2*dy-2*dx
            screen.set_at((round(x),round(y)),white)
    else :
        p=2*dx-dy
       
        for i in range(dy):
            if p<0:
                x=x
                y=y+ly
                p=p+2*dx
            else:
                x=x+lx
                y=y+ly
                p=p+2*dx-2*dy
            screen.set_at((round(x),round(y)),white)


while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.QUIT()
            sys.exit()
    screen.fill(black)
# Outer boundary
    bla_line_draw(50,100,350,100)    # Top boundary
    bla_line_draw(50,250,350,250)    # Bottom boundary
    bla_line_draw(50,100,50,250)     # Left boundary
    bla_line_draw(350,100,350,250)   # Right boundary

# Center line
    bla_line_draw(200,100,200,250)

# Left goal box
    bla_line_draw(50,140,90,140)
    bla_line_draw(50,210,90,210)
    bla_line_draw(90,140,90,210)

# Right goal box
    bla_line_draw(310,140,350,140)
    bla_line_draw(310,210,350,210)
    bla_line_draw(310,140,310,210)

    pygame.display.flip()