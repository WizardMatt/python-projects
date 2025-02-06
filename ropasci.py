import random

choices = ["rock", "paper", "scissors"]

def get_winner(player, computer):
    """Determines the winner between player and computer."""
    if player == computer:
        return "🤝 It's a tie!"
    elif (player == "rock" and computer == "scissors") or \
         (player == "scissors" and computer == "paper") or \
         (player == "paper" and computer == "rock"):
        return "🎉 You win!"
    else:
        return "😢 Computer wins!"

# Game loop
while True:
    print("\n🎮 Rock, Paper, Scissors Game")
    player_choice = input("Enter your choice (rock, paper, scissors or quit): ").lower()

    if player_choice == "quit":
        print("👋 Thanks for playing!")
        break
    elif player_choice not in choices:
        print("❌ Invalid choice! Please try again.")
        continue

    computer_choice = random.choice(choices)
    print(f"🤖 Computer chose: {computer_choice}")
    
    print(get_winner(player_choice, computer_choice))
