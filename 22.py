# №22

firstNumber = input("Enter the first number:")
secondNumber = input("Enter the first number:")
thirdNumber = input("Enter the first number:")

if firstNumber == secondNumber == thirdNumber:
    print(f"Numbers {firstNumber}, {secondNumber} and {thirdNumber} are the same.")
else:
    if firstNumber > secondNumber and firstNumber > thirdNumber:
        print(f"The largest number is {firstNumber}")
    if secondNumber > firstNumber and secondNumber > thirdNumber:
        print(f"The largest number is {secondNumber}")
    else:
        print(f"The largest number is {thirdNumber}")

# Enter the first number: 1
# Enter the second number: 51
# Enter the third number: 2
# The largest number is 51.

