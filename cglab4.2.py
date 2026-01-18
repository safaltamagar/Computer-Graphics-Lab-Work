import pygame
import sys

pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Smiley Face - Midpoint Circle Algorithm")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

def draw_circle_points(xc, yc, x, y):
    screen.set_at((xc + x, yc + y), WHITE)
    screen.set_at((xc - x, yc + y), WHITE)
    screen.set_at((xc + x, yc - y), WHITE)
    screen.set_at((xc - x, yc - y), WHITE)
    screen.set_at((xc + y, yc + x), WHITE)
    screen.set_at((xc - y, yc + x), WHITE)
    screen.set_at((xc + y, yc - x), WHITE)
    screen.set_at((xc - y, yc - x), WHITE)

def midpoint_circle(xc, yc, r):
    x = 0
    y = r
    d = 1 - r

    while x <= y:
        draw_circle_points(xc, yc, x, y)
        x += 1
        if d < 0:
            d += 2 * x + 1
        else:
            y -= 1
            d += 2 * x - 2 * y + 1

# Smile (lower half circle)
def midpoint_smile(xc, yc, r):
    x = 0
    y = r
    d = 1 - r

    while x <= y:
        # Only draw lower half
        screen.set_at((xc + x, yc + y), WHITE)
        screen.set_at((xc - x, yc + y), WHITE)
        screen.set_at((xc + y, yc + x), WHITE)
        screen.set_at((xc - y, yc + x), WHITE)

        x += 1
        if d < 0:
            d += 2 * x + 1
        else:
            y -= 1
            d += 2 * x - 2 * y + 1

def main():
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(BLACK)

        # Face
        midpoint_circle(400, 300, 150)

        # Eyes
        midpoint_circle(350, 260, 15)
        midpoint_circle(450, 260, 15)

        # Smile
        midpoint_smile(400, 320, 60)

        pygame.display.flip()

    pygame.quit()
    sys.exit()

main()
