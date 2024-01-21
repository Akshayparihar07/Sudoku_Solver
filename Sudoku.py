import time
import random

def print_board(board, size=9):
    for i in range(size):
        if i % 3 == 0 and i != 0:
            print('-------------------------')
        for j in range(size):
            if j % 3 == 0 and j != 0:
                print(' | ', end=' ')
            print(board[i][j], end=' ')
        print()

def solve_sudoku(board):
    empty_cell = find_empty(board)

    if not empty_cell:
        return True

    row, col = empty_cell

    for num in range(1, 10):
        position = (row, col)
        if is_valid(board, num, position):
            board[row][col] = num
            if solve_sudoku(board):
                return True
            else:
                board[row][col] = 0
    return False

def is_valid(board, num, position):
    r, c = position

    for i in range(9):
        if board[r][i] == num and c != i:
            return False

        if board[i][c] == num and r != i:
            return False

    box_x, box_y = c // 3, r // 3

    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if i < 9 and j < 9 and board[i][j] == num and (i, j) != position:
                return False
    return True

def find_empty(board):
    for x in range(9):
        for y in range(9):
            if board[x][y] == 0:
                return x, y
    return None

if __name__ == "__main__":
    board =     [[0, 0, 4, 0, 0, 0, 0, 0, 0],
                [2, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 6, 0, 0, 0, 0, 8],
                [0, 0, 0, 0, 0, 0, 5, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 1, 0],
                [0, 9, 8, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 7, 0],
                [0, 0, 0, 0, 3, 0, 0, 0, 2],
                [0, 0, 0, 0, 7, 9, 0, 0, 0]]
    
    print('Original Sudoku:')
    print_board(board)

    solve_sudoku(board)

    print('\nSolving Sudoku⌛')
    time.sleep(2)
    print('\nHere is Your Solved Sudoku🥳')
    print_board(board)
