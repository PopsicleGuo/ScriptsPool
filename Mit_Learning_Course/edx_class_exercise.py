# Class exercise
iteration = 0
while iteration < 5:
    count = 0
    for letter in "hello, world":
        count += 1
        if iteration % 2 == 0:
            break
    print("Iteration " + str(iteration) + "; count is: " + str(count))
    iteration += 1

# Class exercise
# Try to get most close square root number
x = 25
epsilon = 0.01
step = 0.1
guess = 0.0

while abs(guess**2-x) >= epsilon:
    if guess <= x:
        guess += step
    else:
        break

if abs(guess**2 - x) >= epsilon:
    print('failed')
else:
    print('succeeded: ' + str(guess))
print(guess)

# Newton-raphson root guess
epsilon = 0.01
y = 54.0
guess = y/2.0
numGuess = 0

while abs(guess*guess - y) >= epsilon:
    numGuess += 1
    guess = guess - (((guess**2) - y)/(2*guess))
print('Number of Guess: ', numGuess)
print('Square root of ' + str(y) + ' is about '+ str(guess))