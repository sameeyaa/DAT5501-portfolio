import random
import tkinter as tk

options = ["rock", "paper", "scissors"]

def get_computer_option():
    #randomise what the computer chooses
    return random.choice(options)

#when there is a draw
def get_winner(player_option, computer_option):
    if player_option == computer_option:
        return(" It's a draw! Play again")
    
    winner = {
        "rock" : "scissors",
        "paper" : "rock",
        "scissors" : "paper"
    }
    