import time
import random

turns = 10

print("Hello, Let's play hangman! You will have " + str(turns) + " turns!")
print("")

# delay
time.sleep(0.5)

# set of words to guess from
word_list = ["geekflare", "awesome", "python", "magic"]
word = random.choice(word_list)

guessed_letters = set()

# loop till no turns are remaining
while turns > 0:
    wrong = 0

    for char in word:
        if char in guessed_letters:
            print(char, end=" ")
        else:
            print("_", end=" ")
            wrong += 1

    print("\n")

    if wrong == 0:
        print("You won :)")
        break

    guess = input("Guess a character or enter the correct word: ")
    guess = guess.lower()
    
    if len(guess) == 1:
        if guess in word:
            guessed_letters.add(guess)
        else:
            turns -= 1
            print("Wrong")
            print("You have", turns, "turns left!")
    elif len(guess) > 1:
        if guess == word:
            print("You won :)")
            break
        else:
            turns -= 1
            print("Wrong")
            print("You have", turns, "turns left!")
    else:
        print("Invalid input")

if turns == 0:
    print("You Lose :(")
