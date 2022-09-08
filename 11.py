# №11

amountFrom = float(input("How many euros are you exchanging?"))
rateFrom = float(input("What is the exchange rate?"))
print(amountFrom, "euros at an exchange rate of", rateFrom, "is:")
rateTo = 100
amountTo = ((amountFrom * rateFrom) / rateTo)
print(amountTo, "U.S. dollars.")

# How many euros are you exchanging? 81
# What is the exchange rate? 137.51
# 81 euros at an exchange rate of 137.51 is
# 111.38 U.S. dollars.