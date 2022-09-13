# №20

orderAmount = float(input("What is the order amount?"))
state = str(input("What state do you live in?"))
if state == "Wisconsin":
    district = str(input("Forthe county ofresidence?"))
    if district == "Eau Claire":
        tax = (orderAmount * 0.005) / 100
        print(f"The tax is ${tax}.")
        total = tax + orderAmount
        print(f"The total is ${total}.")
    else:
        tax = (orderAmount * 0.004) / 100
        print(f"The tax is ${tax}.")
        total = tax + orderAmount
        print(f"The total is ${total}.")
else:
    tax = (orderAmount * 8) / 100
    print(f"The tax is ${tax}.")
    total = tax + orderAmount
    print(f"The total is ${total}.")

# What is the order amount? 10
# What state do you live in? Wisconsin
# The tax is $0.50.
# The total is $10.50.
