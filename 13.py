# №13
# FIXME
principal = float(input("What is the principal amount?")) #P
rate_of_interest = float(input("What is the rate?")) #r
number_of_years = float(input("What is the number of years?")) #t
compounded_per_year = float(input("What is the number of times the interest is compounded per year?")) #n

result1 = 1 + (rate_of_interest / compounded_per_year) 
result2 = compounded_per_year * number_of_years
result3 = pow(result1 , result2)
result = principal * result3
print(
    f"${principal} invested at {rate_of_interest}% for {number_of_years} years compounded {compounded_per_year} times per year is ${result}."
)

# What is the principal amount? 1500
# What is the rate? 4.3
# What is the number of years? 6
# What is the number of times the interest
# is compounded per year? 4
# $1500 invested at 4.3% for 6 years compounded 4 times per year is $1938.84.
