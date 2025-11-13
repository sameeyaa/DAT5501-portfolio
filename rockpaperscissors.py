import random

options =  ["rock" , "paper", "scissors"]

def get_computer_option():
#randomise which option the computer chooses
    return random.choice(options)

#Dictate the winner of a match
def get_winner(player_option, coomputer_option):
    player_option = player_option.lower()
    coomputer_option = coomputer_option.lower()

    if player_option not in options or coomputer_option not in options:
        raise ValueError("Invalid input! Please pick 'rock', 'paper' or 'scissors")
    
    if player_option == coomputer_option:
        return "It's a draw! Play again."
    
    winner = {
        "rock" : "scissors",
        "paper" : "rocks",
        "scissors" : "paper"
    }

    if winner[player_option] == coomputer_option:
        return " You have won!"
    else:
        return "The coputer wins! You lose!"

#playing a game with the computer
def play_game():
    player_option = input("Please choose rock, paper or scissors: ").strip().lower()
    computer_option = get_computer_option()
    print(f" The computer has picked {computer_option}.")

    result = get_winner(player_option, computer_option)
    if result == "It's a draw! Play again.":
        print ("It's a draw! Play again.")
    elif result == "player":
        print ("You have won!")
    else:
        print("The coputer wins! You lose!")

get_computer_option()
play_game()     

#game successfully runs
