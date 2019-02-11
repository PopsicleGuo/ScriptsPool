
# This question is related 'compound' calculation

balance = 3329
annualInterestRate = 0.2
monInterest = annualInterestRate/12
fixedPayment = 0
intBalance = balance

'''
    You're going to get a right fixed monthly payment for pay back the whole balance in 1 year
The idea is iterate the fixed payment amount with a multiple of $10,
then put fixed payment value into the for loop, 
check the current value of fixedPayment can pay back the balance in 1 year or not
If it's not then continue the while loop to increase the value of fixed payment 
'''

while intBalance > 0:
    intBalance = balance
    fixedPayment += 10
    for i in range(12):
        intBalance -= fixedPayment
        intBalance += intBalance*monInterest
        print(intBalance)
print("Lowest Payment: ", fixedPayment)