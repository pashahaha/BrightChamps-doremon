import random

words = ['apple', 'banana', 'cherry', 'date', 'elderberry']

word = random.choice(words)

name = input("What is your name? ")
guessedLetters = ''

chance = 10

print("Hello " + name + "! Let's play a game of word guess")
while chance > 0:
    guess = input("Guess a letter: ")
    
    guessedLetters = guessedLetters + guess
    
    wrong = 0
    
    for letter in word:
        if letter in guessedLetters:
            print(letter, end=' ')
        else:
            print('_', end=' ')
            wrong += 1
    
    if wrong == 0:
        print("\nYou win!")
        break

    if guess not in word:
        chance -= 1
        print("\nWrong guess. You have " + str(chance) + " chances left")

    if chance == 0:
        print("\nYou lose! The word was " + word)