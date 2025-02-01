import random
import time

# picks a word from the options, converts it to a list
words = ["BRIDE", "AUDIO", "CAPER", "WRITE", "PEACE", "CHOIR", "OCEAN", "WORDY", "VERVE", "SPICE", "BEACH", "QUEST", "MAGMA", "EXACT", "AMISS", "SCRUB", "INDEX", "SNAKY"]

answer = random.choice(words)
answer_list = list(answer)

lives = 3

print(answer)
print(answer_list)

time.sleep(0.5)
print("Welcome to Hangman!")
time.sleep(1)
guess = input("The word is 5 letters long. What is your first guess? ").upper()
time.sleep(0.5)

length = len(answer_list)

# checks the number of lives - ends if there aren't enough left.
# If the input is correct, removes the letter from the list and asks for another input.
# repeats until there are no more lives or if the word is guessed.

while True:
    if lives != 0:
        if guess in answer_list:
            print("The letter", guess, "is correct!")
            answer_list.remove(guess)
            print(answer_list)
            length = len(answer_list)
            print(length)
            if length == 0:
                print("You guessed the word! The word was", answer, ".")
                break
            else:
                time.sleep(1)
                guess = input("What is your next guess? ").upper()
        else:
            print("The letter", guess, "is incorrect!")
            lives -= 1
            time.sleep(0.5)
            print("You have", lives, "tries remaining.")
            time.sleep(1)
            guess = input("What is your next guess? ").upper()
    else:
        print("You ran out of guesses! The word was", answer,".")
        break

time.sleep(0.5)
print("Thanks for playing!")
