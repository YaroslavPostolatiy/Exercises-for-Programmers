# №21

months = [
    "January", "February", "March", "April", "May", "June", "July",
    "August", "September", "October", "November", "December"
          ]
month = int(input("Please enter the number of the month:"))

try:
    print(f"The name of the month is {months[month - 1]}")
except IndexError:
    print("Such a month does not exist")
