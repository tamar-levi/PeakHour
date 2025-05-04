import pygame
from settings import *
from game.car import Car
import json
import os

class Board:
    def __init__(self, level_path):
        self.cars = self.load_level(level_path)

    def load_level(self, path):
        with open(path) as f:
            data = json.load(f)
        cars = []
        for item in data["cars"]:
            car = Car(**item)
            cars.append(car)
        return cars

    def draw(self, surface):
        surface.fill(BG)

        # ציור רשת
        for i in range(ROWS):
            pygame.draw.line(surface, GRID, (0, i * CELL_SIZE), (WIDTH, i * CELL_SIZE))
            pygame.draw.line(surface, GRID, (i * CELL_SIZE, 0), (i * CELL_SIZE, WIDTH))

        # ציור רכבים
        for car in self.cars:
            rect = pygame.Rect(*car.get_rect())
            pygame.draw.rect(surface, car.color, rect, border_radius=8)
            if car.is_red:
                pygame.draw.rect(surface, (0, 0, 0), rect, 3, border_radius=8)

    def get_car_at_pos(self, pos):
        for car in reversed(self.cars):
            rect = pygame.Rect(*car.get_rect())
            if rect.collidepoint(pos):
                return car
        return None

    def is_valid_move(self, car):
        if car.x < 0 or car.y < 0:
            return False
        if car.direction == 'H':
            if car.x + car.length > COLS:
                return False
        else:
            if car.y + car.length > ROWS:
                return False

        for other in self.cars:
            if other == car:
                continue
            if pygame.Rect(*car.get_rect()).colliderect(pygame.Rect(*other.get_rect())):
                return False

        return True

    def is_win(self):
        for car in self.cars:
            if car.is_red:
                return car.x + car.length == COLS
        return False
