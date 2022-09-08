# №9

lengthroom = int(input("What is the length of the room in feet?"))
widthroom = int(input("What is the width of the room in feet?"))
gallon = 350
perimeter = lengthroom * widthroom
if perimeter < gallon:
    print("You will need to purchase 1 gallons of paint to cover", perimeter, "square feet. Remember, you can’t buy a partial gallon of paint. You must round up to the next whole gallon")
else:
    gallons = math.ceil(perimeter / gallon)
    print("You will need to purchase", gallons, "gallons of paint to cover", perimeter, "square feet. Remember, you can’t buy a partial gallon of paint. You must round up to the next whole gallon")

# You will need to purchase 2 gallons of
# paint to cover 360 square feet.
# Remember, you can’t buy a partial gallon of paint. You must
# round up to the next whole gallon.