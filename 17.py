# №17

alcoholDistributionRatioMan = 0.73
alcoholDistributionRatioWoman = 0.66
TruealcoholContent = 0.08

alcoholConsumed = float(input("Total alcohol consumed, in ounces (oz):"))
bodyWeight = float(input("Body weight in pounds:"))
sex = str(input("Sex:"))
hours = float(input("Number of hours since the last drink:"))

if sex == "Man":
    result = (alcoholConsumed * 5.14) / (
        bodyWeight * alcoholDistributionRatioMan
    ) - 0.15 * hours
    if result > TruealcoholContent:
        print(f"Your BAC is {result}. It is not legal for you to drive.")
    else:
        print("It is legal for you to drive.")
else:
    sex == "Woman"
    result = (alcoholConsumed * 5.14) / (
        bodyWeight * alcoholDistributionRatioWoman
    ) - 0.15 * hours
    if result > TruealcoholContent:
        print(f"Your BAC is {result}. It is not legal for you to drive.")
    else:
        print("It is legal for you to drive.")

# Your BAC is 0.08
# It is not legal for you to drive.
