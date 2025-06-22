---
# Snake Game (Tkinter Edition)

A classic Snake Game built using Python's `tkinter` GUI framework. This version includes dynamic food placement, moving snake, blockades, restart capability, user tracking, and persistent score management.

---

##  Features

*  Snake movement with arrow keys
*  Food appears at random safe positions
*  Collision detection with self, walls, and blockades
*  Score tracking in real-time
*  Restart button after game over
*  Enter your name before playing
*  Personal and Global Best Score Tracking
*  Top 5 Players scoreboard (stored in `scores.json`)

---

##  File Structure

```bash
├── game.py              # Main game logic and UI
├── snake.py             # Snake class (movement, rendering)
├── food.py              # Food class with collision-aware placement
├── blockade.py          # Blockade class with random placement
├── score_manager.py     # Handles user scores and JSON I/O
├── scores.json          # Auto-generated file storing player high scores
└── README.md            # You are here!
```

---

##  Evolution of Features

| Stage        | Feature Added                                      |
| ------------ | -------------------------------------------------- |
|  **Step 1** | Basic snake and food                               |
|  **Step 2** | Food avoids snake body                             |
|  **Step 3** | Added random blockades (obstacles)                 |
|  **Step 4** | Restart button after game over                     |
|  **Step 5** | User prompted for name (in-game input)             |
|  **Step 6** | Scores tracked in `scores.json`                    |
|  **Step 7** | Personal Best and Global Best scores displayed     |
|  **Step 8** | Top 5 player leaderboard shown on game over screen |

---

##  Controls

* Use **Arrow Keys** (`← ↑ ↓ →`) to change the snake's direction.
* Press **Restart** after game over to play again.

---

##  How It Works

* When the game starts, you are asked to **enter your name** directly in the game window.
* Your **score increases** as you collect food.
* Your score and best score are stored **permanently** in `scores.json`.
* The **Top 5 players** are shown after each game.

---

##  Customization

###  Change Snake Speed

The snake’s speed is controlled by the global variable:

```python
SPEED = 150  # milliseconds between moves
```

* **Lower** this value to make the snake move **faster**.
* **Increase** it to make the game **slower** and easier.

For example:

```python
SPEED = 100  # Faster
SPEED = 200  # Slower
```

> You can find this in the top of `game.py`.

---

##  Requirements

* Python 3.6+
* No external libraries needed (`tkinter` and `json` are built-in)

---

##  To Run the Game

Make sure all `.py` files are in the same directory.

```bash
python game.py
```

A window will open where you can enter your name and start playing.

---

##  Example Leaderboard (`scores.json`)

```json
{
  "Abhinav": 15,
  "Riya": 8,
  "Aryan": 12,
  "Priya": 10,
  "Shreyas": 18
}
```

---

##  Ideas for Future Additions

*  Background music
*  Multiple levels with increasing speed
*  Snake skin/color customization
*  Pause/resume functionality
*  Power-ups and lives

---

