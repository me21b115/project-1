import random

# Dictionary representing the snake and ladder board
board = {
    3: 22,
    5: 8,
    11: 26,
    20: 29,
    17: 4,
    19: 7,
    27: 1,
    21: 9
}

# Function to roll a dice
def roll_dice():
    return random.randint(1, 6)

# Function to play the game
def play_game():
    player_position = 0
    while player_position < 30:
        # Roll the dice
        dice = roll_dice()
        print("You rolled a", dice)

        # Update the player's position
        player_position += dice

        # Check if the player landed on a snake or ladder
        if player_position in board:
            if player_position < board[player_position]:
                print("Congratulations! You landed on a ladder.")
            else:
                print("Oops! You landed on a snake.")

            # Move the player to the new position
            player_position = board[player_position]

        print("Your current position is", player_position)

        if player_position == 30:
            print("Congratulations! You reached the final position.")
            break

        if player_position > 30:
            print("Oops! You went beyond the final position.")
            break

        print()

# Start the game
play_game()
