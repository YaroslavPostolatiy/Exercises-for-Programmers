# №13
# FIXME
principal = float(input("Enter the principal:"))
rateOfInterest = float(input("Enter the rate of interest:"))
numberOfYears = float(input("Enter the number of years:"))
compoundedPerYear = float(
    input("What is the number of times the interest is compounded per year?")
)
result = principal * (1 + (rateOfInterest / numberOfYears))
print(
    f"After, {numberOfYears}, years at, {rateOfInterest}%, the investment will be worth ${result}"
)

# What is the principal amount? 1500
# What is the rate? 4.3
# What is the number of years? 6
# What is the number of times the interest
# is compounded per year? 4
# $1500 invested at 4.3% for 6 years
# compounded 4 times per year is $1938.84.
