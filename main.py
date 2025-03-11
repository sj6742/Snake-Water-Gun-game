import random
import tkinter as tk
from tkinter import messagebox


def play_game(user_choice):
    choices = {"Snake": 1, "Water": -1, "Gun": 0}
    reversed_choices = {1: "🐍 Snake", -1: "💧 Water", 0: "🔫 Gun"}
    
    computer_choice = random.choice(list(choices.values()))
    user_value = choices[user_choice]


    if user_value == computer_choice:
        result = "It's a Draw! 😐"
    elif (user_value == 1 and computer_choice == -1) or \
        (user_value == -1 and computer_choice == 0) or \
        (user_value == 0 and computer_choice == 1):
        result = "You Win! 🎉"
    else:
        result = "You Lose! 😢"

    result_label.config(text=f"You Chose: {user_choice}\nComputer Chose: {reversed_choices[computer_choice]}\n{result}")


root = tk.Tk()
root.title("Snake-Water-Gun Game 🐍💧🔫")
root.geometry("400x500")
root.configure(bg="#f7e6a1")


title_label = tk.Label(root, text="Snake-Water-Gun Game 🎮", font=("Arial", 18, "bold"), bg="#f7e6a1", fg="#333")
title_label.pack(pady=10)


instruction_label = tk.Label(root, text="Choose your move:", font=("Arial", 14), bg="#f7e6a1", fg="#555")
instruction_label.pack(pady=5)


button_frame = tk.Frame(root, bg="#f7e6a1")
button_frame.pack(pady=10)

snake_btn = tk.Button(button_frame, text="🐍 Snake", font=("Arial", 14), bg="#ffcc66", fg="black", width=10, command=lambda: play_game("Snake"))
snake_btn.grid(row=0, column=0, padx=10, pady=10)

water_btn = tk.Button(button_frame, text="💧 Water", font=("Arial", 14), bg="#66ccff", fg="black", width=10, command=lambda: play_game("Water"))
water_btn.grid(row=0, column=1, padx=10, pady=10)

gun_btn = tk.Button(button_frame, text="🔫 Gun", font=("Arial", 14), bg="#ff6666", fg="black", width=10, command=lambda: play_game("Gun"))
gun_btn.grid(row=0, column=2, padx=10, pady=10)


result_label = tk.Label(root, text="", font=("Arial", 14), bg="#f7e6a1", fg="black", justify="center")
result_label.pack(pady=20)

root.mainloop()
