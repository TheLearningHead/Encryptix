# Task 3: TIC-TAC-TOE AI

## Overview

This project implements the classic game of Tic-Tac-Toe, allowing a human player to play against an unbeatable AI. The AI uses the Minimax algorithm to make optimal moves, ensuring it cannot be defeated if played correctly. This project helps in understanding game theory, basic search algorithms, and the implementation of the Minimax algorithm.

## Features

- Play Tic-Tac-Toe against an AI.
- The AI uses the Minimax algorithm to make optimal moves.
- Simple command-line interface for easy gameplay.
- Detects and announces the winner or a tie game.

## Setup

### Prerequisites

- Python 3 installed on your machine.

### Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/TheLearningHead/Encryptix.git
    ```
2. Navigate to the Task3 directory:
    ```sh
    cd Encryptix/Task3
    ```

## Usage

To start the Tic-Tac-Toe game, run the script:
```sh
python tictactoe_ai.py
```

Example gameplay:
```
The position for each box is as follows: 
 | 1 | 2 | 3 | 
 | 4 | 5 | 6 | 
 | 7 | 8 | 9 | 
Do you want to start the game? (Yes/No): no
AI player is thinking...
 | O |   |   | 
 |   |   |   | 
 |   |   |   | 
Enter your move position (1-9): 5
 | O |   |   | 
 |   | X |   | 
 |   |   |   | 
AI player is thinking...
 | O | O |   | 
 |   | X |   | 
 |   |   |   | 
Enter your move position (1-9): 3
 | O | O | X | 
 |   | X |   | 
 |   |   |   | 
AI player is thinking...
 | O | O | X | 
 |   | X |   | 
 | O |   |   | 
Enter your move position (1-9): 4
 | O | O | X | 
 | X | X |   | 
 | O |   |   | 
AI player is thinking...
 | O | O | X | 
 | X | X | O | 
 | O |   |   | 
Enter your move position (1-9): 9
 | O | O | X | 
 | X | X | O | 
 | O |   | X | 
AI player is thinking...
 | O | O | X | 
 | X | X | O | 
 | O | O | X | 
It's a tie!
```

## Code Explanation

### Main Components

1. **Display Function**
    - `display(grid)`: Prints the current state of the game board.

2. **Move Handling**
    - `no_move_remaining(grid)`: Checks if there are any empty spaces left on the board.
    - `make_move(grid, row, column, player)`: Places a move on the board for the specified player.
    - `check_winner(grid, player)`: Checks if the specified player has won the game.

3. **AI Logic**
    - `minimax(grid, depth, is_maximizing)`: Implements the Minimax algorithm to determine the optimal move for the AI by recursively evaluating the board to maximize the AI's score and minimize the player's score.
    - `ai_move(grid)`: Determines the best move for the AI using the Minimax algorithm.

4. **Game Flow**
    - `play_game()`: Manages the game loop, allowing the human player to make moves and the AI to respond, while checking for win conditions or a tie.

### Function Details

- **`display(grid)`**: 
    - Prints the current state of the Tic-Tac-Toe board in a formatted way.

- **`no_move_remaining(grid)`**:
    - Returns `True` if there are no empty spaces left on the board, otherwise `False`.

- **`make_move(grid, row, column, player)`**:
    - Places a move on the board for the specified player (`X` or `O`).
    - Returns `True` if the move is successful, otherwise `False`.

- **`check_winner(grid, player)`**:
    - Checks all rows, columns, and diagonals to see if the specified player has won the game.
    - Returns `True` if the player has won, otherwise `False`.

- **`minimax(grid, depth, is_maximizing)`**:
    - Implements the Minimax algorithm to evaluate and return the best score for the AI's move.
    - Considers all possible moves and recursively calculates the score for each move to find the optimal one.

- **`ai_move(grid)`**:
    - Determines and returns the best move for the AI by using the Minimax algorithm to evaluate all possible moves.

- **`play_game()`**:
    - Handles the game flow by taking user input for moves, making AI moves, and checking for win/tie conditions.
    - Alternates turns between the human player and the AI.
