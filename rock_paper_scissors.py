import random

def get_user_choice():
    choice = input("Enter Rock, Paper, or Scissors: ").lower()
    while choice not in ["rock", "paper", "scissors"]:
        print("Invalid choice. Try again.")
        choice = input("Enter Rock, Paper, or Scissors: ").lower()
    return choice

def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

def decide_winner(user, computer):
    if user == computer:
        return "draw"
    elif (user == "rock" and computer == "scissors") or \
         (user == "paper" and computer == "rock") or \
         (user == "scissors" and computer == "paper"):
        return "user"
    else:
        return "computer"

user_score = 0
computer_score = 0

while True:
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    print(f"Computer chose: {computer_choice}")

    result = decide_winner(user_choice, computer_choice)
    if result == "user":
        print("You win!")
        user_score += 1
    elif result == "computer":
        print("Computer wins!")
        computer_score += 1
    else:
        print("It's a draw!")

    print(f"Score: You {user_score} - Computer {computer_score}")
    play_again = input("Play again? (yes/no): ").lower()
    if play_again != "yes":
        break
