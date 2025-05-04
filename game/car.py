from settings import CELL_SIZE

class Car:
    def __init__(self, x, y, length, direction, color, is_red=False):
        self.x = x
        self.y = y
        self.length = length
        self.direction = direction
        self.color = color
        self.is_red = is_red

    def get_rect(self):
        if self.direction == 'H':
            return CELL_SIZE * self.x, CELL_SIZE * self.y, CELL_SIZE * self.length, CELL_SIZE
        else:
            return CELL_SIZE * self.x, CELL_SIZE * self.y, CELL_SIZE, CELL_SIZE * self.length

    def move(self, dx, dy, board):
        old_x, old_y = self.x, self.y
        if self.direction == 'H':
            self.x += dx
        else:
            self.y += dy

        if not board.is_valid_move(self):
            self.x, self.y = old_x, old_y
