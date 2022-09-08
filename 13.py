# №13

P = float(input("What is the principal amount?"))
r = float(input("What is the rate?"))
t = float(input("What is the number of years?"))
A = P * (1 + (r * t))
print("After", t, "years at", r, "%", ", the investment will be worth", A)