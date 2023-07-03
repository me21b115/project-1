# Function to print the Tic Tac Toe board
def print_board(board):
    for row in board:
        print("|".join(row))
        print("-" * 9)

# Function to check if there is a winning combination
def check_winner(board):
    # Check rows
    for row in board:
        if row[0] == row[1] == row[2] != " ":
            return row[0]

    # Check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != " ":
            return board[0][col]

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return board[0][2]

    return None

# Function to play the game
def play_game():
    board = [[" ", " ", " "],
             [" ", " ", " "],
             [" ", " ", " "]]

    current_player = "X"
    while True:
        # Print the board
        print_board(board)

        # Get the player's move
        row = int(input("Enter the row (0-2): "))
        col = int(input("Enter the column (0-2): "))

        # Check if the move is valid
        if row < 0 or row > 2 or col < 0 or col > 2 or board[row][col] != " ":
            print("Invalid move. Try again.")
            continue

        # Update the board with the player's move
        board[row][col] = current_player

        # Check if the current player wins
        winner = check_winner(board)
        if winner:
            print("Player", winner, "wins!")
            break

        # Check if the game ends in a tie
        if all(board[row][col] != " " for row in range(3) for col in range(3)):
            print("It's a tie!")
            break

        # Switch to the other player
        current_player = "O" if current_player == "X" else "X"

# Start the game
play_game()
