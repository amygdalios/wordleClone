import tkinter as tk
from tkinter import messagebox
import random

# Load words
def loadWords():
    try:
        with open("words.txt") as f:
            return [word.strip().lower() for word in f if len(word.strip()) == 5]
    except:
        messagebox.showerror("Error", "Word list could not be opened or found.")
        exit()

# Colors
CORRECT_SPOT = "#6aaa64"   # Green
WRONG_SPOT = "#c9b458"     # Yellow
NOT_IN_WORD = "#787c7e"    # Gray
TEXT_COLOR = "white"

# GUI Setup
root = tk.Tk()
root.title("Wordle Clone")
root.geometry("350x500")
root.resizable(False, False)

# Create a frame for the grid
frame = tk.Frame(root)
frame.pack(pady=20)

# Create the 5x6 grid of labels
labels = [[tk.Label(frame, text="", width=4, height=2, font=("Helvetica", 18), relief="groove", borderwidth=2) for _ in range(5)] for _ in range(6)]
for i in range(6):
    for j in range(5):
        labels[i][j].grid(row=i, column=j, padx=3, pady=3)

# Entry + button
guess_var = tk.StringVar()
entry = tk.Entry(root, textvariable=guess_var, font=("Helvetica", 16), justify="center")
entry.pack()

current_row = 0

wordList = loadWords()
secretWord = random.choice(wordList)

def check_guess():
    global current_row
    guess = guess_var.get().lower()

    if len(guess) != 5 or guess not in wordList:
        messagebox.showwarning("Invalid Guess", "Guess must be a valid 5-letter word.")
        return

    for i in range(5):
        letter = guess[i].upper()
        label = labels[current_row][i]
        label.config(text=letter)

        if guess[i] == secretWord[i]:
            label.config(bg=CORRECT_SPOT, fg=TEXT_COLOR)
        elif guess[i] in secretWord:
            label.config(bg=WRONG_SPOT, fg=TEXT_COLOR)
        else:
            label.config(bg=NOT_IN_WORD, fg=TEXT_COLOR)

    if guess == secretWord:
        messagebox.showinfo("🎉 Congrats!", f"You guessed the word: {secretWord.upper()}")
        root.quit()
    elif current_row == 5:
        messagebox.showinfo("Game Over", f"Out of attempts! The word was: {secretWord.upper()}")
        root.quit()
    else:
        current_row += 1
        guess_var.set("")

submit_btn = tk.Button(root, text="Submit", command=check_guess, font=("Helvetica", 14))
submit_btn.pack(pady=10)

entry.bind("<Return>", lambda event: check_guess())

# Focus entry on start
entry.focus()

# Run the app
root.mainloop()