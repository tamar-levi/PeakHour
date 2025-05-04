import pygame
from settings import *

def draw_text(surface, text, size, x, y, color=(255, 255, 255)):
    font = pygame.font.SysFont("arial", size, bold=True)
    text_surface = font.render(text, True, color)
    rect = text_surface.get_rect(center=(x, y))
    surface.blit(text_surface, rect)

def show_screen(screen, title, message):
    screen.fill((0, 0, 0))
    draw_text(screen, title, 48, WIDTH // 2, HEIGHT // 2 - 50)
    draw_text(screen, message, 32, WIDTH // 2, HEIGHT // 2 + 20)
    pygame.display.flip()

    wait = True
    while wait:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                wait = False
            elif event.type == pygame.QUIT:
                pygame.quit()
                exit()
