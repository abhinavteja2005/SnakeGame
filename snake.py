# snake.py
from tkinter import *
SNAKE_COLOR = "#00FF00"
SPACE_SIZE = 50
BODY_PARTS = 3

class Snake:
    def __init__(self, canvas):
        self.canvas = canvas
        self.body_size = BODY_PARTS
        self.coordinates = [[0, 0] for _ in range(BODY_PARTS)]
        self.squares = []
        
        for x, y in self.coordinates:
            square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR, tag="snake")
            self.squares.append(square)
