# Turtle Crossing 

An arcade-style game where the player controls a turtle, aiming to cross a busy road without colliding with cars. The game gets progressively harder as the player completes levels.

## Table of Contents
- [About the Game](#about-the-game)
- [Installation](#installation)
- [How to Play](#how-to-play)
- [File Description](#file-description)
- [License](#license)

## About the Game
The game's objective is to help the turtle cross the road safely. The turtle can only move upwards, and the road is filled with moving cars. Each time the turtle reaches the finish line, the difficulty increases, with cars moving faster and appearing more frequently.

### Features:
- Randomly generated cars with various colors.
- Collision detection between the turtle and the cars.
- Level progression, where the cars move faster each time the player successfully crosses the road.
- Game over screen when the player collides with a car.

## Installation
### Requirements:
- Python 3.8 or higher: The game is written in Python and requires version 3.8 or later for compatibility with features such as file handling and `turtle` graphics.
- `turtle` module (pre-installed with Python)

### Steps:
1. Clone the repository to your local machine.
```bash
git clone https://github.com/dimitra-savvani/Turtle-Crossing-Game.git
```

2. Navigate to the project directory.
```bash
cd Turtle-Crossing-Game
```
3. Run the game.
```bash
python main.py
```

## How to Play
- Use the Up arrow key to move the turtle up.
- The goal is to cross the road without hitting any cars.
- Each time you successfully reach the top, the level increases, and the cars move faster.
- If the turtle collides with a car, the game is over.

## File Description:
- **main.py**: The main entry point of the game, handles the game loop, car generation, collision detection, and level progression.
- **player.py**: Contains the `Player` class, which defines the behavior of the turtle, including its movement and level reset.
- **car_manager.py**: This file contains two classes:
  - The `Car` class, which defines individual cars that move across the screen.
  - The `CarManager` class, which is responsible for managing the creation of new cars and controlling their speed and movement across the screen. It also checks for collisions between the player and the cars.

- **scoreboard.py**: Displays the current level on the screen and shows a "Game Over" message when the game ends.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

This README.md should give users an understanding of the game, how to install and play it, and provide insight into the structure and purpose of each file in the project. Let me know if you need any further changes!
