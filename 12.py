# №12

principal = float(input("Enter the principal:"))
rate_of_interest = float(input("Enter the rate of interest:"))
numberOfYears = float(input("Enter the number of years:"))

result2 = rate_of_interest * numberOfYears
result1 = (result2 * principal) / 100
result = result1 + principal

print(f"After, {numberOfYears}, years at, {rate_of_interest}%, the investment will be worth ${result}")

# Enter the principal: 1500
# Enter the rate of interest: 4.3
# Enter the number of years: 4
# After 4 years at 4.3%, the investment will
# be worth $1758.
