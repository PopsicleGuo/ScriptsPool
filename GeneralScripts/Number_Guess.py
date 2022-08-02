
'''
Small guess tool
'''

min = 0
max = 100
trigger = True

print('Please think of a number between 0 and 100!')
while trigger:
    guess = (min + max)/2
    print('Is your secret number %d' % guess + '?')
    print("Enter 'h' to indicate the guess is too high. "
          "Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
    user_input = input()
    if user_input is 'h':
        max = guess
    elif user_input is 'l':
        min = guess
    elif user_input is 'c':
        trigger = False
        print('Game over. Your secret number was:', guess)
    else:
        print('Please fill right string!')
