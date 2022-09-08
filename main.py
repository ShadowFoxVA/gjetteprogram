import random

# Secret number
secret_number = random.randint(0,10)

# start of program, asking if you want to play a game
print("Hi, what's your name")
name = input("Enter name here: ")
print("Well," {name} "would you like to guess a number")

# 
for guess_taken in range(0,6):
    print("Take a guess")
    guess= int(input())

    if guess < secret_number:
        print("Your guess is too low, try again")
    elif guess > secret_number:
        print("Your guess is too high, try again")
    elif guess <= 0:
        print("That's not a valid number")
    else:
        break

if guess == secret_number:
    print("You guessed right in " + str(guess_taken) "turns {name})
else:
    print("Wrong number, the one I was thinkg of was" + str(secret_number))