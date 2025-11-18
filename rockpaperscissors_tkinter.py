import random
import tkinter as tk

options = ["rock", "paper", "scissors"]

def get_computer_option():
    return random.choice(options)

def get_winner(player_option, computer_option):
    if player_option == computer_option:
        return "draw"
    
    winner = {
        "rock": "scissors",
        "paper": "rock",
        "scissors": "paper"
    }

    if winner[player_option] == computer_option:
        return "player"
    else:
        return "computer"

def play(player_choice):
    computer_choice = get_computer_option()
    computer_label.config(text=f"Computer chose: {computer_choice}")

    result = get_winner(player_choice, computer_choice)

    if result == "draw":
        result_label.config(text="It's a draw!")
    elif result == "player":
        result_label.config(text="You win!")
    else:
        result_label.config(text="Computer wins!")

# ---- GUI ----

root = tk.Tk()     # <-- FIXED
root.title("Rock, Paper, Scissors")
root.geometry("350x250")

tk.Label(root, text="Pick rock, paper or scissors:", font=("Calibri", 14)).pack(pady=10)

button_frame = tk.Frame(root)
button_frame.pack()

tk.Button(button_frame, text="rock", width=10, command=lambda: play("rock")).grid(row=0, column=0, padx=5)
tk.Button(button_frame, text="paper", width=10, command=lambda: play("paper")).grid(row=0, column=1, padx=5)
tk.Button(button_frame, text="scissors", width=10, command=lambda: play("scissors")).grid(row=0, column=2, padx=5)

computer_label = tk.Label(root, text="", font=("Calibri", 14))
computer_label.pack(pady=10)

result_label = tk.Label(root, text="", font=("Calibri", 18))
result_label.pack(pady=10)

root.mainloop()
