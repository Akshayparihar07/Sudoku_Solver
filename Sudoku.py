import random
board = random_boards[random.randint(0, 11)]

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

    # BASE CASE
    find = find_empty(board)

    # IF NOT 0s (EMPTY CELLS FOUND) THEN RETURN TRUE AS WE HAVE REACHED THE END OF OUR BOARD 
    if not find :
        return True
    
    # OTHERWISE TAKE THE ROW AND COL RETURNED BY find_empty() FUNCITON
    else:
        (row, col) = find

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
    r = position[0]
    c = position[1]

    for i in range(9):
        # Checking all the columns of a row  
        if board[r][i] == num and c != i:
            return False

        # checking all the rows of a column 
        if board[i][c] == num and r != i:
            return False

        # Check in the 3x3 grid
        box_x = position[1]
        box_y = position[0]

        for i in range(box_y*3, box_y*3 + 3):
            for j in range(box_x*3, box_x*3 + 3):
                if i < 9 and j < 9 and board[i][j] == num and (i,j) != position:
                    return False
    return True


def find_empty(board):
    for x in range(9):
        for y in range(9):
        # IF FOUND ANY EMPTY SPACE AT ANY PARTICULAR POSITION THEN RETURN THE POSITION 
            if board[x][y] == 0:
                return (x, y)  # this will return the coordinates in the form if a tuple 

    # OTHERWISE REUTRN NOTHING
    return None

if __name__=="__main__":
    print_board(board)
    solve_sudoku(board)
    print()
    print_board(board)