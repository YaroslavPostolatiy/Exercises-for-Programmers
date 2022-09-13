# №18

temperature = str(
    input(
        "Press C to convert from Fahrenheit to Celsius. Press F to convert from Celsius to Fahrenheit."
    ).upper()
)
if temperature == "C":
    Celsius = float(input("Please enter the temperature in Celsius:"))
    result = (Celsius * (9 / 5)) + 32
    print(
        f"The temperature in Celsius is: {Celsius}",
    )
    print(f"The temperature in Fahrenheit is: {result}")
elif temperature == "F":
    Fahrenheit = float(input("Please enter the temperature in Fahrenheit:"))
    result = (Fahrenheit - 32) * (5 / 9)
    print(
        f"The temperature in Fahrenheit is: {Fahrenheit}",
    )
    print(f"The temperature in Celsius is: {result}")
else:
    print("You pressed the wrong button")

# Press C to convert from Fahrenheit to Celsius.
# Press F to convert from Celsius to Fahrenheit.
# Your choice: C
# Please enter the temperature in Fahrenheit: 32
# The temperature in Celsius is 0.
