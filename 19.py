# №19

weight = float(input("Your weight:"))
height = float(input("Your height:"))

body_mass_index = (weight / (height * height)) * 703

if body_mass_index < 19.5:
    print("You should see your doctor.")
elif body_mass_index >= 19.5 and body_mass_index <= 32.5:
    print("You are within the ideal weight range.")
else:
    print("You are overweight. You should see your doctor.")

# Your BMI is 19.5.
# You are within the ideal weight range.
# or
# Your BMI is 32.5.
# You are overweight. You should see your doctor.