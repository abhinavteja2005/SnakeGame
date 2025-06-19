from tkinter import *
import random

SPACE_SIZE = 50
BLOCKADE_COLOR = "#888888"
GAME_WIDTH = 700
GAME_HEIGHT = 700

class Blockade:
    def __init__(self, canvas, count=5):
        self.coordinates = []
        for _ in range(count):
            while True:
                x = random.randint(0, (GAME_WIDTH // SPACE_SIZE) - 1) * SPACE_SIZE
                y = random.randint(0, (GAME_HEIGHT // SPACE_SIZE) - 1) * SPACE_SIZE
                # No need to check for overlap with food or snake here
                break
            self.coordinates.append([x, y])
            canvas.create_rectangle(
                x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=BLOCKADE_COLOR, tag="blockade"
            )
