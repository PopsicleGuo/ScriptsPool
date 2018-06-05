# Problem 3 - Using Bisection Search to Make the Program Faster
# Calatue low and upper variables for bisection search
# The idea is try to use bisection search to get monthly fixed payment
balance = 999999
annualInterestRate = 0.18
monInterest = annualInterestRate/12.0
intbalance = balance
guessed = False
low = balance/12.0
upper = (balance * (1 + monInterest)**12) / 12.0
guess = round((low+upper)/2, 2)
epsilon = 0.03

'''
      Try to use first guess as monthly payment for the loop.
    After loop calculation, if the balance is greater than 0, that means the balance still has money left, 
    we have to set low variable to 'guess' variable to do next bisection search.
      If the balance is less than 0, that means monthly payment is a bit higher, 
    the rest balance has been paid without 12 months, so we have to change 'low' variable with guess value
      The problem is the balance never becomes to 0, we have to select a number very close to 0. 
    like from 0 to 0.1.  
'''

while not guessed:
    guess = round((low+upper)/2, 2)
    print("every new guess value: ", guess)
    intbalance = balance
    for i in range(12):
        intbalance -= guess
        intbalance += monInterest*intbalance
        print(intbalance)
    if abs(intbalance) < 0.1:
        guessed = True
    elif intbalance < 0:
        upper = guess
    else:
        low = guess
print("Lowest Payment: ", guess)