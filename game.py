from tkinter import *
from snake import Snake
from blockade import Blockade
from food import Food

GAME_WIDTH = 700
GAME_HEIGHT = 700
SPEED = 150
SPACE_SIZE = 50
BACKGROUND_COLOR = "#000000"

def next_turn(snake, food, blockades):
    global direction, score

    x, y = snake.coordinates[0]

    if direction == "up":
        y -= SPACE_SIZE
    elif direction == "down":
        y += SPACE_SIZE
    elif direction == "left":
        x -= SPACE_SIZE
    elif direction == "right":
        x += SPACE_SIZE

    snake.coordinates.insert(0, [x, y])
    square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill="#00FF00")
    snake.squares.insert(0, square)

    if x == food.coordinates[0] and y == food.coordinates[1]:
        score += 1
        label.config(text=f"Score: {score}")
        canvas.delete("food")
        food = Food(canvas, snake, blockades)
    else:
        del snake.coordinates[-1]
        canvas.delete(snake.squares[-1])
        del snake.squares[-1]

    if check_collisions(snake, blockades):
        game_over()
    else:
        window.after(SPEED, next_turn, snake, food, blockades)

def check_collisions(snake, blockades):
    x, y = snake.coordinates[0]

    if x < 0 or x >= GAME_WIDTH or y < 0 or y >= GAME_HEIGHT:
        return True

    for part in snake.coordinates[1:]:
        if part == [x, y]:
            return True

    for bx, by in blockades.coordinates:
        if [x, y] == [bx, by]:
            return True

    return False

def change_direction(new_direction):
    global direction
    opposites = {"up": "down", "down": "up", "left": "right", "right": "left"}
    if direction != opposites.get(new_direction):
        direction = new_direction

def game_over():
    canvas.delete(ALL)
    canvas.create_text(
        GAME_WIDTH / 2,
        GAME_HEIGHT / 2,
        font=('consolas', 70),
        text="GAME OVER",
        fill="red",
        tag="gameover"
    )

# --- Main Program ---
window = Tk()
window.title("Snake Game")
window.resizable(False, False)

score = 0
direction = 'down'

label = Label(window, text=f"Score: {score}", font=('consolas', 40))
label.pack()

canvas = Canvas(window, bg=BACKGROUND_COLOR, height=GAME_HEIGHT, width=GAME_WIDTH)
canvas.pack()

window.update()
window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
x = int((screen_width / 2) - (window_width / 2))
y = int((screen_height / 2) - (window_height / 2))
window.geometry(f"{window_width}x{window_height}+{x}+{y}")

# Key bindings
window.bind('<Left>', lambda e: change_direction("left"))
window.bind('<Right>', lambda e: change_direction("right"))
window.bind('<Up>', lambda e: change_direction("up"))
window.bind('<Down>', lambda e: change_direction("down"))

# Initialize game objects
snake = Snake(canvas)
blockades = Blockade(canvas, count=5)
food = Food(canvas, snake, blockades)

# Start game
next_turn(snake, food, blockades)

window.mainloop()
