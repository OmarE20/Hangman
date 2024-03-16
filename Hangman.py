import tkinter as tk
from tkinter import messagebox
import random

class HangmanGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Hangman Game")
        self.master.config(bg="#2C3E50")  # Dark background color
        self.word_list = ["python", "hangman", "computer", "programming", "developer", "interface", "keyboard"]
        self.secret_word = random.choice(self.word_list)
        self.guess_word = ["_" for _ in self.secret_word]
        self.attempts_left = 6
        self.guess_label_var = tk.StringVar()
        self.guess_label_var.set(" ".join(self.guess_word))
        
        self.create_widgets()

    def create_widgets(self):
        self.word_label = tk.Label(self.master, textvariable=self.guess_label_var, font=("Helvetica", 24), bg="#2C3E50", fg="white")
        self.word_label.pack(pady=10)

        self.guess_entry = tk.Entry(self.master, font=("Helvetica", 18), bg="#34495E", fg="white")
        self.guess_entry.pack(pady=5)

        self.guess_button = tk.Button(self.master, text="Guess", command=self.check_guess, bg="#2980B9", fg="white", font=("Helvetica", 14))
        self.guess_button.pack(pady=5)

        self.attempts_label = tk.Label(self.master, text=f"Attempts left: {self.attempts_left}", font=("Helvetica", 14), bg="#2C3E50", fg="white")
        self.attempts_label.pack(pady=5)

        self.canvas = tk.Canvas(self.master, width=200, height=300, bg="#2C3E50")
        self.canvas.pack()

    def check_guess(self):
        guess = self.guess_entry.get().lower()
        if len(guess) == 1:
            if guess in self.secret_word:
                for i in range(len(self.secret_word)):
                    if self.secret_word[i] == guess:
                        self.guess_word[i] = guess
                self.guess_label_var.set(" ".join(self.guess_word))
                if "_" not in self.guess_word:
                    self.game_over("You Win!")
            else:
                self.attempts_left -= 1
                self.attempts_label.config(text=f"Attempts left: {self.attempts_left}")
                self.draw_hangman()
                if self.attempts_left == 0:
                    self.game_over("You Lose!")
        else:
            messagebox.showwarning("Invalid Input", "Please enter only one letter.")
        
        # Clear the text box after processing the guess
        self.guess_entry.delete(0, tk.END)

    def draw_hangman(self):
        if self.attempts_left == 5:
            # Head
            self.canvas.create_oval(50, 50, 150, 150, outline="white", width=2)
        elif self.attempts_left == 4:
            # Body
            self.canvas.create_line(100, 150, 100, 250, fill="white", width=2)
        elif self.attempts_left == 3:
            # Left Arm
            self.canvas.create_line(100, 175, 50, 225, fill="white", width=2)
        elif self.attempts_left == 2:
            # Right Arm
            self.canvas.create_line(100, 175, 150, 225, fill="white", width=2)
        elif self.attempts_left == 1:
            # Left Leg
            self.canvas.create_line(100, 250, 50, 300, fill="white", width=2)
        elif self.attempts_left == 0:
            # Right Leg
            self.canvas.create_line(100, 250, 150, 300, fill="white", width=2)

    def game_over(self, message):
        messagebox.showinfo("Game Over", message)
        self.master.destroy()

def main():
    root = tk.Tk()
    root.config(bg="#2C3E50")  # Dark background color
    hangman_game = HangmanGame(root)
    root.mainloop()

if __name__ == "__main__":
    main()
