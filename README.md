# ECE276B SP23 Project 1

## Overview
In this assignment, you are required to implement dynammic programming for the Door-Key problems.
<p align="center">
<img src="gif/doorkey.gif" alt="Door-key Problem" width="500"/></br>
</p>

There are 7 test scenes you have to test and include in the report.

|           doorkey-5x5-normal            |
| :-------------------------------------: |
| <img src="envs/known_envs/doorkey-5x5-normal.png"> |

|           doorkey-6x6-normal            |            doorkey-6x6-direct            |            doorkey-6x6-shortcut            |
| :-------------------------------------: | :--------------------------------------: | :----------------------------------------: |
| <img src="envs/known_envs/doorkey-6x6-normal.png"> | <img src="envs/known_envs/doorkey-6x6-direct.png" > | <img src="envs/known_envs/doorkey-6x6-shortcut.png" > |

|           doorkey-8x8-normal            |            doorkey-8x8-direct            |            doorkey-8x8-shortcut            |
| :-------------------------------------: | :--------------------------------------: | :----------------------------------------: |
| <img src="envs/known_envs/doorkey-8x8-normal.png"> | <img src="envs/known_envs/doorkey-8x8-direct.png" > | <img src="envs/known_envs/doorkey-8x8-shortcut.png" > |

## Installation

- Install Python version `3.7 ~ 3.10`
- Install dependencies
```bash
pip install -r requirements.txt
```

## Run code:
```bash
python3 doorkey.py
```

## Source code description:
- **doorkey.py**: Main function.
- **planning.py**: DP algorithm door key problem.
- **test.ipynb**: Debug and test functions.
- **example.py**: Shows you how to interact with the utilities in utils.py, and also gives you some examples of interacting with gym-minigrid directly.
- **utils.py**: Functions for file loading, env plotting, gif plotting, etc.