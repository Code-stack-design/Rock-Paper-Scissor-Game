import random

# Choices and emojis
choices = {
    "rock": "🪨",
    "paper": "📄",
    "scissors": "✂️",
    "lizard": "🦎",
    "spock": "🖖"
}

# Rules dictionary
win_conditions = {
    "rock": ["scissors", "lizard"],
    "paper": ["rock", "spock"],
    "scissors": ["paper", "lizard"],
    "lizard": ["paper", "spock"],
    "spock": ["rock", "scissors"]
}

# Display choices
def display_choices():
    print("\nChoose one of the following:")
    for idx, choice in enumerate(choices.keys(), 1):
        print(f"{idx}. {choice.capitalize()} {choices[choice]}")

# Get user's choice
def get_user_choice():
    while True:
        try:
            display_choices()
            user_input = int(input("Enter your choice number: "))
            if 1 <= user_input <= len(choices):
                return list(choices.keys())[user_input - 1]
            else:
                print("Invalid number. Try again.")
        except ValueError:
            print("Invalid input. Enter a number.")

# Determine winner
def determine_winner(player, computer):
    if player == computer:
        return "tie"
    elif computer in win_conditions[player]:
        return "player"
    else:
        return "computer"

# Get score limit from user
def get_score_limit():
    while True:
        try:
            score_limit = int(input("🎯 Enter the score to win the game (e.g., 5): "))
            if score_limit > 0:
                return score_limit
            else:
                print("Score must be a positive number.")
        except ValueError:
            print("Invalid input. Please enter a number.")

# Game loop
def play_game():
    print("🎮 Welcome to Rock Paper Scissors Lizard Spock!")
    score_to_win = get_score_limit()

    player_score = 0
    computer_score = 0
    ties = 0

    while player_score < score_to_win and computer_score < score_to_win:
        player_choice = get_user_choice()
        computer_choice = random.choice(list(choices.keys()))

        print(f"\nYou chose: {player_choice.capitalize()} {choices[player_choice]}")
        print(f"Computer chose: {computer_choice.capitalize()} {choices[computer_choice]}")

        result = determine_winner(player_choice, computer_choice)

        if result == "tie":
            print("It's a tie!")
            ties += 1
        elif result == "player":
            print("You win this round! 🎉")
            player_score += 1
        else:
            print("Computer wins this round! 💻")
            computer_score += 1

        # Show current score
        print(f"\n🔢 Score: You {player_score} - {computer_score} Computer | 🤝 Ties: {ties}")

    # Final result
    print("\n🎉 Game Over!")
    if player_score == score_to_win:
        print("🏆 Congratulations! You reached the winning score!")
    else:
        print("💻 The computer reached the winning score. Better luck next time!")

    print(f"\n📊 Final Score: You {player_score} - {computer_score} Computer | Ties: {ties}")

if __name__ == "__main__":
    play_game()
