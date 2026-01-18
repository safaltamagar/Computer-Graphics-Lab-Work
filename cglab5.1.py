import pygame
import sys

pygame.init()
WIDTH, HEIGHT = 600, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Midpoint Ellipse Algorithm")
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

def plot_points(xc,yc,x,y):
    screen.set_at((xc + x, yc + y), WHITE)
    screen.set_at((xc - x, yc + y), WHITE)
    screen.set_at((xc + x, yc - y), WHITE)
    screen.set_at((xc - x, yc - y), WHITE)

def midpoint_ellipse(xc,yc,rx,ry):
    x=0
    y=ry
    rx2= rx*rx
    ry2= ry*ry
    two_rx2 = 2 * rx2
    two_ry2 = 2 * ry2    

    #region 1
    p1=ry2-rx2*ry + 0.25*rx2

    while (two_ry2*x) < (two_rx2*y):
        plot_points(xc,yc,x,y)
        if p1<0:
            x=x+1
            y=y
            p1=p1+two_ry2*x+ry2
        else:
            x=x+1
            y=y-1
            p1=p1+ two_ry2*x - two_rx2*y + ry2
    #region 2
    p2 = ry2 * (x + 0.5)**2 + rx2 * (y - 1)**2 - rx2 * ry2

    while y>=0:
        plot_points(xc,yc,x,y)
        if p2>0:
            x=x
            y=y-1
            p2=p2-two_rx2*y+x
        else:
            x=x+1
            y=y-1
            p2=p2+two_ry2*x-two_rx2*y+rx2

def main():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(BLACK)
        midpoint_ellipse(200,100,100,50)   
        pygame.display.flip()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
    

