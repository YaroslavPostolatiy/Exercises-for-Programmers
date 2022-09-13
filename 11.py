# №11

amount_from = float(input("How many euros are you exchanging?"))
rate_from = float(input("What is the exchange rate?"))

print(amount_from, "euros at an exchange rate of", rate_from, "is:")

rateTo = 100
amountTo = ((amount_from * rate_from) / rateTo)

print(amountTo, "U.S. dollars.")

# How many euros are you exchanging? 81
# What is the exchange rate? 137.51
# 81 euros at an exchange rate of 137.51 is
# 111.38 U.S. dollars.