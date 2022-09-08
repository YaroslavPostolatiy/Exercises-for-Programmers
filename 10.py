# №10

priceofitem1 = float(input("Enter the price of item 1:"))
quantityofitem1 = float(input("Enter the quantity of item 1:"))
priceofitem2 = float(input("Enter the price of item 2:"))
quantityofitem2 = float(input("Enter the quantity of item 2:"))
priceofitem3 = float(input("Enter the price of item 3:"))
quantityofitem3 = float(input("Enter the quantity of item 3:"))
item1 = priceofitem1 * quantityofitem1
item2 = priceofitem2 * quantityofitem2
item3 = priceofitem3 * quantityofitem3
subtotal = item1 + item2 + item3
print("Subtotal:", subtotal)
tax = float(subtotal * 5.5 / 100)
print("Tax:", tax)
total = float(subtotal + tax)
print("Total:", total)

# Enter the price of item 1: 25
# Enter the quantity of item 1: 2
# Enter the price of item 2: 10
# Enter the quantity of item 2: 1
# Enter the price of item 3: 4
# Enter the quantity of item 3: 1
# Subtotal: $64.00
# Tax: $3.52
# Total: $67.52
