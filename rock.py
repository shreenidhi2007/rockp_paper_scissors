import random

# Function to display rules of the game
def game_rules():
    print("#"*50)
    print("\nWelcome to the game of Rock, Paper, Scissors ")
    print("Rules of the Game:")
    print(" Rock beats Scissors")
    print(" Scissors beats Paper")
    print(" Paper beats Rock")
    print("\nType 'exit' anytime to quit the game.")
    print("#" * 50)

# Function to get player's choice 
def input_player_choice():
    while True:
        player_choice = input("Enter your choice (rock/paper/scissors/exit): ")
        choice_lst=["rock", "paper", "scissors", "exit"]
        if player_choice in choice_lst :
            return player_choice
        else:
            print("Invalid choice! Please type rock, paper, scissors, or exit.")

# Function to get computer's choice
def input_computer_choice():
    return random.choice(["rock", "paper", "scissors"])



# Function to find the winner
def check_winner(player, computer):
    if player == computer:
        return "draw"
    elif (player == "rock" and computer == "scissors") or (player == "scissors" and computer == "paper") or (player == "paper" and computer == "rock"):
        return "winner_player"
    else:
        return "winner_computer"

# Function to display result of the game in each round
def show_result(player, computer, winner):
    print("\nPlayer's choice:",player)
    print("\nComputer's choice: ",computer)

    if winner == "draw":
        print("\n It's a draw!")
    elif winner == "winner_player":
        print("Player wins this round!")
    else:
        print("Computer wins this round!")

# Main game loop
def rpc_game():
    player_score = 0
    computer_score = 0
    rounds = 0
    #Function call to diplay game rules
    game_rules()

    while True:
        player_choice = input_player_choice()      # Function call to get player choice
        if player_choice == "exit":
            print("\n THANKS! VISIT AGAIN")
            break

        computer_choice = input_computer_choice()    # Function call to get computer input
        winner = check_winner(player_choice, computer_choice)

        show_result(player_choice, computer_choice, winner)   #Function call to display result

        # Score Calculation
        rounds += 1
        if winner == "winner_player":
            player_score += 1           # Updating Player Score
        elif winner == "winner_computer":
            computer_score += 1         # Updating Computer Score
            
        print("#"*50)
        print("\n Scoreboard after ",rounds,"round")
        print("\n Player's Score:",player_score)
        print("\n Computer's Score:",computer_score)
        print("#"*50)

# Run the game
if __name__ == "__main__":
    rpc_game()
