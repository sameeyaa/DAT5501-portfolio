import random

options =  ["rock" , "paper", "scissors"]

def get_game_choice():
#randomise which option the computer chooses
    return random.choice(options)

#Dictate the winner of a match
def get_winner(player_option, coomputer_option):
    player_option = player_option.lower()
    coomputer_option = compile.lower()

    if player_option not in options or coomputer_option not in options:
        raise ValueError("Invalid input! Please pick 'rock', 'paper' or 'scissors")
    