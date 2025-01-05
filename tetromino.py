import random
from colors import COLORS

class Tetromino:
    SHAPES = [
        [[1, 1, 1, 1]],  # I
        [[1, 1], [1, 1]],  # O
        [[1, 1, 1], [0, 1, 0]],  # T
        [[1, 1, 1], [1, 0, 0]],  # L
        [[1, 1, 1], [0, 0, 1]],  # J
        [[1, 1, 0], [0, 1, 1]],  # S
        [[0, 1, 1], [1, 1, 0]]   # Z
    ]

    def __init__(self):
        self.shape_index = random.randint(0, len(self.SHAPES) - 1)
        self.shape = [row[:] for row in self.SHAPES[self.shape_index]]
        self.color = COLORS[self.shape_index]
        
        # Starting position
        self.x = 3
        self.y = -len(self.shape)
    
    def move(self, dx, dy):
        self.x += dx
        self.y += dy
    
    def rotate(self, direction=1):
        # Transpose the matrix
        self.shape = list(zip(*self.shape))
        
        # Reverse rows for clockwise rotation
        if direction > 0:
            self.shape = [list(reversed(row)) for row in self.shape]
        else:
            self.shape = list(reversed(self.shape)) 