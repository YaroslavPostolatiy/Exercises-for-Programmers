# №26

import math

dailyRate = int(input("What is the APR on the card (as a percent)?"))
balance = int(input("What is your balance?"))
monthlyPayment = int(input("What is the monthly payment you can make?"))

# numberOfMonths = ((-1 / 30) * ((math.log(1 + (balance / monthlyPayment) * (1 - (pow(1 + dailyRate, 30))))) / (math.log(1 + dailyRate))))
# numberOfMonths = ((- 1 / 30)) * (math.log(1 + (balance / monthlyPayment) * (1 - pow(1 + dailyRate, 30)) * (math.log(1 + dailyRate))))
numberOfMonths1 = 1 - pow(1 + dailyRate, 30)
numberOfMonths2 = 1 + (balance / monthlyPayment) * (numberOfMonths1)
numberOfMonths3 = math.log (numberOfMonths2)
numberOfMonths4 = math.log(1 + dailyRate)
numberOfMonths5 = numberOfMonths3 / numberOfMonths4
numberOfMonths6 = -( 1 / 30) * numberOfMonths5
print(f"It will take you {numberOfMonths6} months to pay off this card.")

# What is your balance? 5000
# What is the APR on the card (as a percent)? 12
# What is the monthly payment you can make? 100
# It will take you 70 months to pay off this card.


