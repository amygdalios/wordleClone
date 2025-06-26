import random

def openWordList():
    try:
        with open("words.txt") as f:
            wordList = [word.strip().lower() for word in f if len(word.strip()) == 5]
            return wordList
    except:
        print("Word list could not be opened or found.")
        exit()

def pickWord():
    wordList = openWordList()
    return random.choice(wordList)

def get_feedback(guess, secret):
    feedback = []
    for i in range(5):
        if guess[i] == secret[i]:
            feedback.append("🟩")
        elif guess[i] in secret:
            feedback.append("🟨")
        else:
            feedback.append("⬛")
    return "".join(feedback)

def validateInput(guess):
    wordList = openWordList()
    if guess in wordList:
        return True
    else:
        return False

def playGame():
    secretWord = pickWord()
    
    for _ in range(6):
        guess = input(">>> ").lower()
        while not validateInput(guess):
            print("Invalid input. Make sure you typed in a 5 letter word")
            guess = input(">>> ").lower()
        
        feedback = get_feedback(guess, secretWord)
        print(feedback)

        if guess == secretWord:
            print("🎉 You guessed the word!")
            return
    
    print(f"❌ Out of attempts. The word was {secretWord}")

if __name__ == "__main__":
    playGame()