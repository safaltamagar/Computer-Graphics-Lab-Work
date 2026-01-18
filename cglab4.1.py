import pygame
import sys

pygame.init()
WIDTH, HEIGHT = 500, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Midpoint Circle Algorithm")
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

def midpoint_circle(xc, yc, r):
    x = 0
    y = r
    d = 1 - r
    draw_circle_points(xc, yc, x, y)

    while x <=y:
        x += 1
        if d < 0:
            d = d + 2 * x + 1
        else:
            y -= 1
            d = d + 2 * x - 2 * y + 1
        draw_circle_points(xc, yc, x, y)

def draw_circle_points(xc, yc, x, y):
    
    screen.set_at((xc + x, yc + y), WHITE)
    screen.set_at((xc - x, yc + y), WHITE)
    screen.set_at((xc + x, yc - y), WHITE)
    screen.set_at((xc - x, yc - y), WHITE)
    screen.set_at((xc + y, yc + x), WHITE)
    screen.set_at((xc - y, yc + x), WHITE)
    screen.set_at((xc + y, yc - x), WHITE)
    screen.set_at((xc - y, yc - x), WHITE)

def main():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(BLACK)
        midpoint_circle(150,150,100)   
        pygame.display.flip()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()