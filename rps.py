import tkinter as tk
import random
tie_count=0
def play_rps(user_choice):
    global tie_count
    computer_choice = random.choice(["rock", "paper", "scissors"])
    user_label.config(text=f'You chose: {user_choice}')
    computer_label.config(text=f'Computer chose: {computer_choice}')
    if user_choice == computer_choice:
        result_label.config(text="It's a tie!")
        tie_count+=1
        tie_label.config(text=f'tie score {tie_count}')
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        result_label.config(text="You win!")
        user_score_label.config(text=f'Your score: {str(int(user_score_label.cget("text").split()[-1]) + 1)}')
    else:
        result_label.config(text="Computer wins!")
        computer_score_label.config(text=f"Computer's score: {str(int(computer_score_label.cget('text').split()[-1]) + 1)}")
def play_again():
    user_label.config(text='')
    computer_label.config(text='')
    result_label.config(text='')
root = tk.Tk()
root.title("Rock, Paper, Scissors")
user_score_label = tk.Label(root, text="Your score: 0")
user_score_label.pack()
computer_score_label = tk.Label(root, text="Computer's score: 0")
computer_score_label.pack()
user_choice_label = tk.Label(root, text="Choose rock, paper, or scissors:")
user_choice_label.pack()
choices = ["rock", "paper", "scissors"]
for choice in choices:
    button = tk.Button(root, text=choice, command=lambda choice=choice: play_rps(choice))
    button.pack()
play_again_button = tk.Button(root, text="Play Again", command=play_again)
play_again_button.pack()
user_label = tk.Label(root, text="")
user_label.pack()
computer_label = tk.Label(root, text="")
computer_label.pack()
result_label = tk.Label(root, text="")
result_label.pack()
tie_label = tk.Label(root, text="")
tie_label.pack()
root.mainloop()
