# Initialize the Tic Tac Toe board
board = [
    ['-', '-', '-'],
    ['-', '-', '-'],
    ['-', '-', '-']
]

# Variable to track current player (X starts first)
current_player = 'X'

def print_board():
    # Print the current board state
    for row in board:
        print(' '.join(row))
    print()

def check_winner(player):
    # Check if the current player has won horizontally, vertically, or diagonally
    for i in range(3):
        if all(board[i][j] == player for j in range(3)):
            return True
        if all(board[j][i] == player for j in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2-i] == player for i in range(3)):
        return True
    return False

def is_board_full():
    # Check if the board is full (tie condition)
    for row in board:
        if '-' in row:
            return False
    return True

def reset_board():
    # Reset the board for a new game
    global board, current_player
    board = [
        ['-', '-', '-'],
        ['-', '-', '-'],
        ['-', '-', '-']
    ]
    current_player = 'X'

def tic_tac_toe():
    global current_player

    print("Welcome to Tic Tac Toe!")
    print_board()

    while True:
        # Get player move
        row = int(input(f"Player {current_player}, enter row (1-3): ")) - 1
        col = int(input(f"Player {current_player}, enter column (1-3): ")) - 1

        # Validate move
        if 0 <= row < 3 and 0 <= col < 3 and board[row][col] == '-':
            board[row][col] = current_player
            print_board()

            # Check for winner
            if check_winner(current_player):
                print(f"Player {current_player} wins!")
                break

            # Check for tie
            if is_board_full():
                print("It's a tie!")
                break

            # Switch player
            current_player = 'O' if current_player == 'X' else 'X'
        else:
            print("Invalid move. Please try again.")

    # Ask for new game
    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again == 'yes':
        reset_board()
        tic_tac_toe()
    else:
        print("Thank you for playing Tic Tac Toe!")

# Start the game
if __name__ == "__main__":
    tic_tac_toe()
