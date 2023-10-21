import random

def get_user_choice():
    choice = input("Enter your choice (rock, paper, or scissor): ").lower()
    while choice not in ['rock', 'paper', 'scissor']:
        print("Invalid choice. Please try again.")
        choice = input("Enter your choice (rock, paper, or scissor): ").lower()
    return choice

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissor'])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissor') or \
         (user_choice == 'scissor' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
     return "You win!"
    else:
     return "You lose!"

def play_game():
    user_wins = 0
    computer_wins = 0
    user_total = 0  
    computer_total=0
    
    print("+-------------------+-------------------+-------------------+-------------------+")
    print("| Your choice       | Your result       | Computer choice   | Computer result   |")
    print("+-------------------+-------------------+-------------------+-------------------+")
    
    for _ in range(3):  
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        
        result = determine_winner(user_choice, computer_choice)
        if result == "You win!":
            user_total += 1  
            print(f"| {user_choice.ljust(18)}| 1{' '*17}| {computer_choice.ljust(18)}| 0{' '*17}|")
        elif result == "You lose!":
            computer_total += 1
            print(f"| {user_choice.ljust(18)}| 0{' '*17}| {computer_choice.ljust(18)}| 1{' '*17}|")
        else:
            print(f"| {user_choice.ljust(18)}| 0{' '*17}| {computer_choice.ljust(18)}| 0{' '*17}|")
    
    print("+-------------------+-------------------+-------------------+-------------------+")
    
    if user_total > computer_total:
        print(f"| Overall Winner: You |")
    elif user_total < computer_total:
        print(f"| Overall Winner: Computer |")
    else:
        print(f"| Overall Result: Tie |")
    print("+-------------------+-------------------+-------------------+-------------------+")

play_game()