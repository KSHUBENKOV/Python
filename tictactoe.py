def print_board(board):
    """Print the game board."""
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board, player):
    """Check if the given player has won."""
    # Check rows, columns, and diagonals
    for i in range(3):
        if all([spot == player for spot in board[i]]) or \
                all([board[j][i] == player for j in range(3)]):
            return True
    if board[0][0] == board[1][1] == board[2][2] == player or \
            board[0][2] == board[1][1] == board[2][0] == player:
        return True
    return False

def tic_tac_toe():
    # Initialize the board
    board = [[' ' for _ in range(3)] for _ in range(3)]
    current_player = 'X'
    moves = 0

    print("Welcome to Tic-Tac-Toe!")
    print_board(board)

    while moves < 9:
        try:
            # Get the user's move
            row = int(input(f"Player {current_player}, enter the row (0, 1, 2): "))
            col = int(input(f"Player {current_player}, enter the column (0, 1, 2): "))

            # Validate the move
            if board[row][col] == ' ':
                board[row][col] = current_player
                print_board(board)
                moves += 1

                # Check if the current player has won
                if check_winner(board, current_player):
                    print(f"Player {current_player} wins!")
                    return

                # Switch players
                current_player = 'O' if current_player == 'X' else 'X'
            else:
                print("Invalid move! Spot already taken. Try again.")
        except (ValueError, IndexError):
            print("Invalid input! Please enter numbers between 0 and 2.")

    print("It's a draw!")

# Run the game
if __name__ == "__main__":
    tic_tac_toe()
