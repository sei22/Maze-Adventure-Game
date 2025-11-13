# Maze Adventure Game

A 2D maze game developed in Python using **[Pyxel](https://github.com/kitao/pyxel?tab=readme-ov-file)**. The maze is **randomly generated** for each new game, providing a unique experience every time. 
Click here to play the game : https://sei22.github.io/Maze-Adventure-Game/my-pyxel-game.html

## Gameplay

- The player is represented by a **small orange square**.
- The maze is **mostly dark**, so the player can only see a limited area around them.
- The player can **place a torch once** using the **Space key**, which permanently lights up part of the maze.
- The maze contains **enemies**. If the player touches an enemy, they die and must restart the level.

## Levels

The game has **three increasing levels of difficulty**, each introducing new types of enemies:

1. **Level 1**  
   - Enemy 1: Moves **randomly**.  
   - Enemy 2: Always **turns right**.

2. **Level 2**  
   - Enemy 1: Moves randomly.  
   - Enemy 2: Turns right.  
   - Enemy 3: **Chases the player**, calculating the path directly to them.

3. **Level 3**  
   - All enemies from previous levels.  
   - Enemy 4: **Spawns directly on the player**, increasing the challenge.

## Bonus Features

- After completing the game, a **bonus ending** is displayed as a **shooting sequence**, including credits and the names of the authors.

## Controls

- **Arrow keys**: Move the player  
- **Space**: Place a permanent torch to light up the maze  
- **Q**: Quit the game  

## How to Run

1. Clone the repository:  
```bash
git clone https://github.com/your-username/my-pyxel-game.git
cd my-pyxel-game
```

2. Create and activate a Python 3.11 environment:

```bash
python3.11 -m venv pyxel_env
source pyxel_env/bin/activate
```

3. Install dependencies:
   
```bash
pip install -r requirements.txt
```

4. Run the game:
```bash
python JeuLaby.py
```
