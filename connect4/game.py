import random

# Constants for the players
PLAYER_1 = "Y"  # AI Player
PLAYER_2 = "B"  # Human Player
EMPTY = 0  # Empty space

# The Connect Four board (6 rows x 7 columns)
ROW_COUNT = 6
COLUMN_COUNT = 7

def create_board():
    return [[EMPTY] * COLUMN_COUNT for _ in range(ROW_COUNT)]

def print_board(board):
    for row in board:
        print(' '.join(str(cell) for cell in row))
    print()

def is_valid_move(board, column):
    return board[0][column] == EMPTY

def get_next_open_row(board, column):
    for row in range(ROW_COUNT-1, -1, -1):
        if board[row][column] == EMPTY:
            return row
    return -1  # Column is full

def drop_piece(board, row, column, piece):
    board[row][column] = piece

def winning_move(board, piece):
    # Check horizontal, vertical, and diagonal connections for a win
    for row in range(ROW_COUNT):
        for col in range(COLUMN_COUNT-3):
            if all(board[row][col+i] == piece for i in range(4)):
                return True

    for row in range(ROW_COUNT-3):
        for col in range(COLUMN_COUNT):
            if all(board[row+i][col] == piece for i in range(4)):
                return True

    for row in range(ROW_COUNT-3):
        for col in range(COLUMN_COUNT-3):
            if all(board[row+i][col+i] == piece for i in range(4)):
                return True

    for row in range(3, ROW_COUNT):
        for col in range(COLUMN_COUNT-3):
            if all(board[row-i][col+i] == piece for i in range(4)):
                return True
    return False

def is_full(board):
    return all(board[0][col] != EMPTY for col in range(COLUMN_COUNT))


# Minimax Algorithm with Alpha-Beta Pruning
def minimax(board, depth, maximizing_player, alpha, beta):
    valid_moves = [col for col in range(COLUMN_COUNT) if is_valid_move(board, col)]
    is_terminal = winning_move(board, PLAYER_1) or winning_move(board, PLAYER_2) or is_full(board)
    
    if depth == 0 or is_terminal:
        if winning_move(board, PLAYER_1):
            return (None, 100000000000000)
        elif winning_move(board, PLAYER_2):
            return (None, -100000000000000)
        elif is_full(board):
            return (None, 0)
        else:
            return (None, evaluate_board(board))

    if maximizing_player:  # AI's turn
        value = -float('inf')
        column = random.choice(valid_moves)
        for col in valid_moves:
            row = get_next_open_row(board, col)
            temp_board = [r[:] for r in board]
            drop_piece(temp_board, row, col, PLAYER_1)
            new_score = minimax(temp_board, depth-1, False, alpha, beta)[1]
            if new_score > value:
                value = new_score
                column = col
            alpha = max(alpha, value)
            if beta <= alpha:
                break
        return column, value
    else:  # Human's turn
        value = float('inf')
        column = random.choice(valid_moves)
        for col in valid_moves:
            row = get_next_open_row(board, col)
            temp_board = [r[:] for r in board]
            drop_piece(temp_board, row, col, PLAYER_2)
            new_score = minimax(temp_board, depth-1, True, alpha, beta)[1]
            if new_score < value:
                value = new_score
                column = col
            beta = min(beta, value)
            if beta <= alpha:
                break
        return column, value

def evaluate_board(board):
    score = 0
    for row in range(ROW_COUNT):
        for col in range(COLUMN_COUNT):
            if board[row][col] == PLAYER_1:
                score += 1  # You can expand this evaluation function
            elif board[row][col] == PLAYER_2:
                score -= 1
    return score

# AI vs Human
def ai_turn(board):
    col, _ = minimax(board, 4, True, -float('inf'), float('inf'))
    row = get_next_open_row(board, col)
    drop_piece(board, row, col, PLAYER_1)
    print(f"AI plays in column {col}")
    print_board(board)

def human_turn(board):
    while True:
        try:
            col = int(input(f"Choose a column (0-{COLUMN_COUNT-1}): "))
            if is_valid_move(board, col):
                row = get_next_open_row(board, col)
                drop_piece(board, row, col, PLAYER_2)
                break
            else:
                print("Column is full! Choose a different one.")
        except ValueError:
            print("Invalid input! Please enter a number.")
    print_board(board)

def play_game():
    board = create_board()
    print_board(board)

    while True:
        ai_turn(board)
        if winning_move(board, PLAYER_1):
            print("AI wins!")
            break
        if is_full(board):
            print("It's a draw!")
            break

        human_turn(board)
        if winning_move(board, PLAYER_2):
            print("You win!")
            break
        if is_full(board):
            print("It's a draw!")
            break

#Execute the game
play_game()
