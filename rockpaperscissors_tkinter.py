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

   #if player or computer win
    if winner[player_option] == computer_option:
        return "player"
    else:
        return "computer"

#create a GUI
root = tk.Tk
root.title("Rock, Paper, Scissors")

#creating the header of the game
tk.Label(root, text = "Pick rock, paper or scissors:", font = ("Calibri", 14))

button_frame = tk.Frame(root)
button_frame.pack()

tk.Button(button_frame, text = "rock", width = 10, command = lambda: play("rock")).grid(row = 0, column = 0, padx = 5)
tk.Button(button_frame, text = "paper", width = 10, command = lambda: play("paper")).grid(row = 0, column = 1, padx = 5)
tk.Button(button_frame, text = "scissors", width = 10, command = lambda: play("paper")).grid(row = 0, column = 2, padx = 5)

computer_label = tk.Label(root, text = "", font = ("Calibri" , 14))
computer_label.pack(pady = 10)

result_label = tk.Label(root, text = "", font = ("Calibri", 18))
result_label.pack(pady = 10)

root.mainloop()