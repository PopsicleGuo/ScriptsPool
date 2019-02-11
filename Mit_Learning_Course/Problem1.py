
# Set total amount and annual interest rate, then you can get monthly rate simply
balance = 5000
annualInterestRate = 0.18
monthlyPaymentRate = 0.02
#
# For each month, calculate statements on the monthly payment and remaining balance.
# At the end of 12 months, print out the remaining balance.
# Be sure to print out no more than two decimal digits of accuracy
# A summary of the required math is found below:
# Monthly interest rate= (Annual interest rate) / 12.0
# Minimum monthly payment = (Minimum monthly payment rate) x (Previous balance)
# Monthly unpaid balance = (Previous balance) - (Minimum monthly payment)
# Updated balance each month = (Monthly unpaid balance) + (Monthly interest rate x Monthly unpaid balance)
#
for i in range(1, 13):
    balance = balance - (balance * monthlyPaymentRate)
    # print("Month " + str(i) + " Remaining balance: ", round(balance, 2))
    anInterest = (annualInterestRate/12)*balance
    balance += anInterest
print("Remaining balance: ", round(balance, 2))



