# №12

P = float(input("Enter the principal:"))
r = float(input("Enter the rate of interest:"))
t = float(input("Enter the number of years:"))
A = P * (1 + (r * t))
print("After", t, "years at", r, "%", ", the investment will be worth", A)

# Enter the principal: 1500
# Enter the rate of interest: 4.3
# Enter the number of years: 4
# After 4 years at 4.3%, the investment will
# be worth $1758.
