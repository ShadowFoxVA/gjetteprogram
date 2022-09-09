import sjekkomriktig
import tilfeldig
import riktig

# start of program, asking if you want to play a game
print("Hi, what's your name")
name = input("Enter name here: ")
print("Well, " + name + " would you like to guess a number between 1 and 10")

# loop that takes in number and check if correct with max attempts
max = 6
secretNumber = tilfeldig.tilfeldig()
for attempts in range(1, max+1):
    print("Take a guess")
    guess = int(input())
    i = sjekkomriktig.check_if_in_range(attempts, secretNumber, guess, max)
    if i == "true":
        break

riktig.check_if_correct (attempts, secretNumber, guess, name)