board = [
    [0, 9, 0, 6, 0, 0, 8, 0, 0],
    [0, 0, 0, 5, 0, 3, 4, 0, 0],
    [8, 0, 7, 0, 0, 0, 6, 1, 0],
    [0, 0, 0, 0, 5, 0, 0, 0, 7],
    [0, 0, 0, 7, 9, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 6, 3, 0, 0],
    [0, 7, 0, 0, 0, 0, 0, 2, 0],
    [0, 4, 0, 0, 0, 0, 0, 0, 0],
    [2, 0, 3, 0, 6, 1, 0, 0, 4]
]

def is_board_valid(board):
    """
        Check the puzzle whether it is valid or not.
    """
    not_empty = []
    for i in range(len(board)):
        for j in range(len(board[0])):
            if not str(board[i][j]).isdigit():
                return False
            
            if board[i][j] != 0:
                not_empty.append((i, j))

    for row, col in not_empty:
        if not valid(board, board[row][col], (row, col)):
            return False
    return True

def print_board(board):
    """
        Print the puzzle as 3x3 box.
    """
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print("-------------------------")
        for j in range(len(board[0])):
            if j % 3 == 0:
                print("| ", end='')
            if j == 8:
                print(str(board[i][j]) + " | ")
            else:
                print(board[i][j], end=' ')

def find_empty(board):
    """
        Find empty spaces to fill valid numbers.
    """
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i, j)  # row, col
    return None

def valid(board, num, pos):
    """
        Check the inserted number whether it is valid or not.
    """
    #check row
    for i in range(len(board[0])):
        if board[pos[0]][i] == num and pos[1] != i:
            return False

    #check column
    for i in range(len(board)):
        if board[i][pos[1]] == num and pos[0] != i:
            return False

    #check box
    box_x = pos[1] // 3
    box_y = pos[0] // 3
    
    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x*3, box_x*3 + 3):
            if board[i][j] == num and (i, j) != pos:
                return False

    return True

def solve(board):
    """
        Solve the puzzle by filling valid numbers.
    """
    empty = find_empty(board)
    if not empty:
        return True
    else:
        row, col = empty
    
    for i in range(1, 10):
        if valid(board, i, (row, col)):
            board[row][col] = i
        
            if solve(board): #backtracking
                return True

        board[row][col] = 0
    
    return False


print("\n*********** PUZZLE ***********")
print_board(board)
if is_board_valid(board):
    solve(board)
    print("\n********** SOLUTION **********")
    print_board(board)
else:
    print("This puzzle is not valid.")