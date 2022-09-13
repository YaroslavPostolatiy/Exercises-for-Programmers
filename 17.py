# №17

alcohol_distribution_ratioMan = 0.73
alcohol_distribution_ratioWoman = 0.66
TruealcoholContent = 0.08

alcohol_consumed = float(input("Total alcohol consumed, in ounces (oz):"))
body_weight = float(input("Body weight in pounds:"))
sex = str(input("Sex:"))
hours = float(input("Number of hours since the last drink:"))

if sex == "Man":
    result = ((alcohol_consumed * 5.14) / (body_weight * alcohol_distribution_ratioMan) - 0.15 * hours)
    if result > TruealcoholContent:
        print(
            f"Your BAC is {result}. It is not legal for you to drive."
            )
    else:
        print("It is legal for you to drive.")
else:
    sex == "Woman"
    result = ((alcohol_consumed * 5.14) / (body_weight * alcohol_distribution_ratioWoman) - 0.15 * hours)
    if result > TruealcoholContent:
        print(
            f"Your BAC is {result}. It is not legal for you to drive."
            )
    else:
        print("It is legal for you to drive.")

# Your BAC is 0.08
# It is not legal for you to drive.