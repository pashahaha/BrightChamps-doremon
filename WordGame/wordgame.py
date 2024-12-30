import random

words = ['Aardvark', 'Bubble', 'Cactus', 'Dolphin', 'Eagle']

word = random.choice(words)

name = input("What is your name? ")

guessedLetters = ''

chance = 10

print("Hello " + name + "! Let's play a game of word guess")
while chance > 0:
    print("You have " + str(chance) + " chances left")
    chance = chance - 1
    guess = input("Guess a letter: ")

print('test')