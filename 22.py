# №22

first_number = input("Enter the first number:")
second_number = input("Enter the second number:")
third_number = input("Enter the third number:")

if first_number == second_number == third_number:
    print(f"Numbers {first_number}, {second_number} and {third_number} are the same.")
else:
    largest = max(first_number, second_number, third_number)
    print(f"The largest number is {largest}")

# Enter the first number: 1
# Enter the second number: 51
# Enter the third number: 2
# The largest number is 51.

