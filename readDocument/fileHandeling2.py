def opening_file():
    f = open("beliver.txt", "r")
    data =f.read()
    print(data)
    f.close()

opening_file()

def letter_count():
    f = open("beliver.txt", "r")
    data = f.read()
    print("The number of letter in the string is:",len(data))
    f.close()

letter_count()

def word_count():
    f = open("beliver.txt", "r")
    data = f.read()
    print("The number of word in the string is:",len(data.split()))
    f.close()

word_count()

def lower_case():
    f = open("beliver.txt", "r")
    data = f.read()
    #print("The number of lower case in the string is:",len([letter for letter in data if letter.islower()]))
    count = 0
    for letter in data:
        if letter.islower():
            count += 1
    print("The number of lower case in this string is:", count)
    f.close()

lower_case()

def nom_words():
    f = open("beliver.txt", "r")
    data = f.read()

    count = 0
    ws = input("Enter the word you want to count: ")
    for word in data.split():
        if ws.lower() == word.lower():
            count += 1

    print("The number of", ws, "in this string is:", count)
    f.close()

nom_words()