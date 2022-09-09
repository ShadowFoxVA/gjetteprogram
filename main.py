import sjekkomintastriktig
import tilfeldig
import sjekkriktig

highscoreAttempts = (0)

runAgain = "yes"
# start of program, asking if you want to play a game
print("Hi, what's your name")
name = input("Enter name here: ")

while runAgain == "yes": 
    print("Well, " + name + " would you like to guess a number between 1 and 10")

    print("Highscore: " + str(highscoreAttempts))

    # loop that takes in number and check if correct with max attempts
    max = 6
    secretNumber = tilfeldig.tilfeldig()
    for attempts in range(1, max+1):
        print("Take a guess")
        guess = int(input())
        i = sjekkomintastriktig.check_if_in_range(attempts, secretNumber, guess, max)
        if i == "true":
            break

    if sjekkriktig.check_if_correct (attempts, secretNumber, guess, name) == "true":
        if highscoreAttempts == 0:
            highscoreAttempts = attempts
        elif highscoreAttempts > attempts:
            highscoreAttempts = attempts

    restart = input("Do you want to try again: ")
    
    if restart == "no":
        print("Thanks for playing :)")
        break