import pygame
pygame.init()

grid_size = 50

def draw_grid(surface, grid_size):
    width, height = surface.get_size()
    for x in range(0, width, grid_size):
        pygame.draw.line(surface, (100, 100, 100), (x, 0), (x, height))
    for y in range(0, height, grid_size):
        pygame.draw.line(surface, (100, 100, 100), (0, y), (width, y))
