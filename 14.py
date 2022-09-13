# №14

order_amount = float(input("What is the order amount?"))
state = str(input("What is the state?"))

if state == "WI":
    print(f"The subtotal is ${order_amount}.")
    tax = ((order_amount * 5.5) / 100)
    print(f"Податок становить ${tax}.")
    total = tax + order_amount
    print(f"The total is ${total}.")
else:
    print(f"The total is ${order_amount}")

# What is the order amount? 10
# What is the state? WI
# The subtotal is $10.00.
# The tax is $0.55.
# The total is $10.55.
# Or
# What is the order amount? 10
# What is the state? MN
# The total is $10.00