def check_if_correct(attempts, secretNumber, guess, name):

    if guess == secretNumber:
        print("You guessed right in " + str(attempts) + " turns " + name)
    else:
        print("Wrong number, the one I was thinkg of was " + str(secretNumber))