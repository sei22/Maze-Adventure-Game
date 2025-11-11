# Maze Adventure Game

A 2D maze game developed in Python using **Pyxel**. The maze is **randomly generated** for each new game, providing a unique experience every time.

## Gameplay

- The player is represented by a **small orange square**.
- The maze is **mostly dark**, so the player can only see a limited area around them.
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

## Controls

- **Arrow keys**: Move the player  
- **Q**: Quit the game  

## How to Run

1. Clone the repository:  
```bash
git clone https://github.com/your-username/my-pyxel-game.git
cd my-pyxel-game

