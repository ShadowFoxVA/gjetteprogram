
def check_if_in_range(attempts, secretNumber, guess, max):
    
    if guess <= 0 or guess > 10:
        print("That's not a valid number, you have " + str(max - attempts) + " left" )
    elif guess < secretNumber:
        print("Your guess is too low, you have " + str(max - attempts) + " left")
    elif guess > secretNumber:
        print("Your guess is too high, you have " + str(max - attempts) + " left")
    else:
        return("true")