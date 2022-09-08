import random

# Secret number
secret_number = random.randint(0,10)

# start of program, asking if you want to play a game
print("Hi, what's your name")
name = input("Enter name here: ")
print("Well, " + name + " would you like to guess a number between 1 and 10")

# 
max = 6
for attempts in range(1, max):
    print("Take a guess")
    guess= int(input())

    if guess <= 0 or guess > 10:
        print("That's not a valid number, you have " + str(max - attempts) + " left" )
    elif guess < secret_number:
        print("Your guess is too low, you have " + str(max - attempts) + " left")
    elif guess > secret_number:
        print("Your guess is too high, you have " + str(max - attempts) + " left")
    else:
        break

if guess == secret_number:
    print("You guessed right in " + str(attempts) + " turns " + name)
else:
    print("Wrong number, the one I was thinkg of was " + str(secret_number))