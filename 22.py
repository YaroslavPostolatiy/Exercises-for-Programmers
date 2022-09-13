# №22

# FIXME: Three times first number
firstNumber = input("Enter the first number:")
secondNumber = input("Enter the first number:")
thirdNumber = input("Enter the first number:")

if firstNumber == secondNumber == thirdNumber:
    print(f"Numbers {firstNumber}, {secondNumber} and {thirdNumber} are the same.")
else:
    largest = max(firstNumber, secondNumber, thirdNumber)
    print(f"The largest number is {largest}")

# Enter the first number: 1
# Enter the second number: 51
# Enter the third number: 2
# The largest number is 51.
