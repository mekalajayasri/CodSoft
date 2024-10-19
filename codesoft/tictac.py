# Tic-Tac-Toe game using if-else statements

# Function to print the game board
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

# Function to check if a player has won
def check_winner(board, player):
    # Check rows
    for row in board:
        if all(s == player for s in row):
            return True

    # Check columns
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    # Check diagonals
    if all(board[i][i] == player for i in range(3)) or all(board[i][2-i] == player for i in range(3)):
        return True
    return False

# Function to check if the board is full (i.e., a tie)
def check_tie(board):
    return all(cell != ' ' for row in board for cell in row)

# Function to play Tic-Tac-Toe
def play_game():
    # Initialize the game board (3x3 grid)
    board = [[' ' for _ in range(3)] for _ in range(3)]

    current_player = 'X'
    game_over = False

    while not game_over:
        print_board(board)
        print(f"Player {current_player}'s turn.")

        # Get row and column input from the player
        row = int(input("Enter the row (0, 1, 2): "))
        col = int(input("Enter the column (0, 1, 2): "))
         # Check if the selected cell is empty
        if board[row][col] == ' ':
            board[row][col] = current_player
        else:
            print("Cell already taken! Try again.")
            continue

        # Check if the current player has won
        if check_winner(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            game_over = True
        # Check if the game is a tie
        elif check_tie(board):
            print_board(board)
            print("It's a tie!")
            game_over = True
        else:
            # Switch to the other player
            current_player = 'O' if current_player == 'X' else 'X'
# Start the game
play_game()
