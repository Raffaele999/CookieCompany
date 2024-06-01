import random

def play_round(player_choice):
    choices = ['rock', 'paper', 'scissors']
    computer_choice = random.choice(choices)
    
    print("You chose:", player_choice)
    print("Computer chose:", computer_choice)

    if player_choice == computer_choice:
        return "It's a tie!"
    elif (player_choice == 'rock' and computer_choice == 'scissors') or \
         (player_choice == 'paper' and computer_choice == 'rock') or \
         (player_choice == 'scissors' and computer_choice == 'paper'):
        return "You win!"
    else:
        return "Computer wins!"

if __name__ == "__main__":
    print("Welcome to Rock, Paper, Scissors!")
    print("Enter your choice (rock, paper, or scissors):")
    user_choice = input().lower()

    if user_choice not in ['rock', 'paper', 'scissors']:
        print("Invalid choice. Please choose either rock, paper, or scissors.")
    else:
        result = play_round(user_choice)
        print(result)
