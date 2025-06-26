import random
from colorama import init, Fore, Style

init(autoreset=True)

def openWordList():
    try:
        with open("words.txt") as f:
            return [word.strip().lower() for word in f if len(word.strip()) == 5]
    except:
        print("Word list could not be opened or found.")
        exit()

def get_colored_feedback(guess, secret):
    feedback = ""
    for i in range(5):
        if guess[i] == secret[i]:
            feedback += Fore.GREEN + guess[i].upper() + Style.RESET_ALL
        elif guess[i] in secret:
            feedback += Fore.YELLOW + guess[i].upper() + Style.RESET_ALL
        else:
            feedback += Fore.LIGHTBLACK_EX + guess[i].upper() + Style.RESET_ALL
    return feedback

def playGame():
    wordList = openWordList()
    secretWord = random.choice(wordList)

    print("Welcome to Wordle (Terminal Edition)!")
    for _ in range(6):
        guess = input(">>> ").lower()
        while guess not in wordList:
            print("Invalid input. Make sure you typed in a 5-letter word")
            guess = input(">>> ").lower()

        feedback = get_colored_feedback(guess, secretWord)
        print(feedback)

        if guess == secretWord:
            print("🎉 You guessed the word!")
            return

    print(f"❌ Out of attempts. The word was {secretWord.upper()}")

if __name__ == "__main__":
    playGame()
