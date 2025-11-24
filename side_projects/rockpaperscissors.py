import random

options =  ["rock" , "paper", "scissors"]

def get_computer_option():
#randomise which option the computer chooses
    return random.choice(options)

#Dictate the winner of a match
def get_winner(player_option, computer_option):
    player_option = player_option.lower()
    computer_option = computer_option.lower()

    if player_option not in options or computer_option not in options:
        raise ValueError("Invalid input! Please pick 'rock', 'paper' or 'scissors")
    
    if player_option == computer_option:
        return "It's a draw! Play again."
    
    winner = {
        "rock" : "scissors",
        "paper" : "rock",
        "scissors" : "paper"
    }

    if winner[player_option] == computer_option:
        return "player"
    else:
        return "The computer wins! You lose!"

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
        print("The computer wins! You lose!")

get_computer_option()
play_game()     

#game successfully runs
