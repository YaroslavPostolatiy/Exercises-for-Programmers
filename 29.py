# №29

stated_rate_of_return = input("What is the rate of return?")
x = stated_rate_of_return.isdigit()
if stated_rate_of_return.isdigit() == False:
    print("Sorry. That's not a valid input.")
elif stated_rate_of_return == "0":
    print("Sorry. That's not a valid input.")
else:
    years = 72 / int(stated_rate_of_return)
    print(f"It will take {years} years to double your initial investment.")