# Sudoku Solver

## Overview
This is a simple Python script to solve Sudoku puzzles using a backtracking algorithm. Sudoku is a logic-based combinatorial number-placement puzzle. The objective is to fill a 9×9 grid with digits so that each column, each row, and each of the nine 3×3 subgrids that compose the grid (also called "boxes", "blocks", or "regions") contain all of the digits from 1 to 9.

## How it Works
- The script defines a Sudoku board as a 9x9 grid represented by a nested list of integers.
- The `print_board()` function prints the Sudoku board in a visually appealing format.
- The `solve_sudoku()` function uses backtracking to recursively solve the Sudoku puzzle. It finds an empty cell, attempts to place a number (1 to 9) in that cell, checks if the placement is valid according to Sudoku rules, and proceeds recursively until the puzzle is solved.
- The `is_valid()` function checks whether placing a number in a given position on the board is valid according to Sudoku rules.
- The `find_empty()` function finds an empty cell (cell with value 0) on the board.
- The main script initializes a Sudoku puzzle, prints the original board, solves the puzzle, and then prints the solved board.

## Usage
1. Clone or download this repository to your local machine.
2. Make sure you have Python installed.
3. Run the script `Sudoku.py`.

## Author
This project is authored by [Akshay Parihar](https://github.com/Akshayparihar07).


