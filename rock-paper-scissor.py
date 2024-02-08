import tkinter as tk
from tkinter import messagebox
import random

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!", user_choice, computer_choice
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return "You win!", user_choice, computer_choice
    else:
        return "Computer wins!", user_choice, computer_choice

def play_game(user_choice):
    computer_choice = random.choice(['rock', 'paper', 'scissors'])
    result, user_choice, computer_choice = determine_winner(user_choice, computer_choice)
    messagebox.showinfo("Result", f"Your choice: {user_choice}\nComputer's choice: {computer_choice}\n\n{result}")

def main():
    root = tk.Tk()
    root.title("Rock Paper Scissors")
    
    label = tk.Label(root, text="Choose your move:")
    label.pack()

    buttons_frame = tk.Frame(root)
    buttons_frame.pack()

    choices = ['rock', 'paper', 'scissors']
    for choice in choices:
        button = tk.Button(buttons_frame, text=choice.capitalize(), width=10,
                           command=lambda ch=choice: play_game(ch))
        button.pack(side=tk.LEFT, padx=5, pady=5)

    root.mainloop()

if __name__ == "__main__":
    main()
