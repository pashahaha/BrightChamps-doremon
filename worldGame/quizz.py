print("Hello, welcome to the quizz game!")
ans = input("are you ready? (yes/no) ")

score = 0
totalguess = 3

if ans.lower() == "yes" or ans.lower() == "y":
    print('Good luck!')
    print("You have " + str(totalguess) + " chances left")
    ans = input("1. What is the most known programming language? ")
    if ans.lower() == "python":
        print("Correct answer")
        score += 1
        print("score: " + str(score))
        print("totalguess: " + str(totalguess))
    else:
        print("Wrong answer")
        totalguess -= 1
        print("score: " + str(score))
        print("totalguess: " + str(totalguess))
    
    ans = input("2. what is 8 * 9? ")
    if ans.lower() == "72":
        print("Correct answer")
        score += 1
        print("score: " + str(score))
        print("totalguess: " + str(totalguess))
    else:
        print("Wrong answer")
        totalguess -= 1
        print("score: " + str(score))
        print("totalguess: " + str(totalguess))

    ans = input("3. What is the capital of Indonesia? ")
    if ans.upper() == "IKN" or ans.lower() == "ibu kota nusantara":
        print("Correct answer")
        score += 1
        print("score: " + str(score))
        print("totalguess: " + str(totalguess))
    else:
        print("Wrong answer")
        totalguess -= 1
        print("score: " + str(score))
        print("totalguess: " + str(totalguess))