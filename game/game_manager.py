import pygame
from settings import *
from game.board import Board
from game.ui import draw_text, show_screen
import os

class GameManager:
    def __init__(self):
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
        pygame.display.set_caption("Rush Hour")
        self.clock = pygame.time.Clock()
        self.level_index = 0
        self.levels = self.load_levels()
        self.board = Board(self.levels[self.level_index])
        self.selected_car = None

    def load_levels(self):
        return [os.path.join("levels", f) for f in sorted(os.listdir("levels")) if f.endswith(".json")]

    def run(self):
        show_screen(self.screen, "Peak hour", "Click to start")
        running = True
        global WIDTH, HEIGHT, CELL_SIZE  # כדי שנוכל לעדכן אותם

        while running:
            self.clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    running = False

                elif event.type == pygame.VIDEORESIZE:
                    WIDTH, HEIGHT = event.w, event.h
                    CELL_SIZE = min(WIDTH // COLS, HEIGHT // ROWS)
                    self.screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)

                elif event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    self.selected_car = self.board.get_car_at_pos(pos)

                elif event.type == pygame.MOUSEBUTTONUP:
                    self.selected_car = None

                elif event.type == pygame.MOUSEMOTION and self.selected_car:
                    mx, my = pygame.mouse.get_pos()
                    rect = pygame.Rect(*self.selected_car.get_rect())
                    if self.selected_car.direction == 'H':
                        # חישוב התנועה על ציר ה-X
                        dx = (mx - rect.centerx) // CELL_SIZE
                        self.selected_car.move(dx, 0, self.board)
                    else:
                        # חישוב התנועה על ציר ה-Y
                        dy = (my - rect.centery) // CELL_SIZE
                        self.selected_car.move(0, dy, self.board)

            self.board.draw(self.screen)
            pygame.display.flip()

            if self.board.is_win():
                show_screen(self.screen, "You won!", "Click to continue")
                self.level_index += 1
                if self.level_index < len(self.levels):
                    self.board = Board(self.levels[self.level_index])
                else:
                    show_screen(self.screen, "You have completed all the steps!", "Kol Hakavod!")
                    running = False
