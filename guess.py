# Biesction function
def magicGuess():
    print("Please think of a number between 0 and 100!")
    low = 0
    high = 100
    guessed = False

    while not guessed:
        guess = (high + low) // 2
        print("Is your secret number: " + str(guess) + "?")
        userChoose = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
        if userChoose == 'c':
            guessed = True
        elif userChoose == 'h':
            high = guess
        elif userChoose == 'l':
            low = guess
        else:
            print("Sorry, I did not understand your input")
    print("Game over. Your secret number was: ", guess)