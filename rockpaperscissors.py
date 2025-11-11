import random

options =  ["rock" , "paper", "scissors"]

def get_game_choice():
    " Pick rock,paper or scsissors and see if the computer will beat you!"
    return random.choice(options)