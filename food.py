# food.py
from tkinter import *
import random

SPACE_SIZE = 50
FOOD_COLOR = "#FF0000"
GAME_WIDTH = 700
GAME_HEIGHT = 700

class Food:
    def __init__(self, canvas, snake, blockades):
        while True:
            x = random.randint(0, (GAME_WIDTH // SPACE_SIZE) - 1) * SPACE_SIZE
            y = random.randint(0, (GAME_HEIGHT // SPACE_SIZE) - 1) * SPACE_SIZE
            # avoid food to respawn on blockade or snake
            if [x, y] in blockades.coordinates:
                continue
            if [x, y] in snake.coordinates:
                continue

            break

        self.coordinates = [x, y]
        canvas.create_oval(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=FOOD_COLOR, tag="food")
