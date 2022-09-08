# №8

numberofpeople = int(input("How many people?"))
amountofpizza = int(input("How many pizzas do you have?"))
slicesofpizza = amountofpizza * 8 #шматочків піци
perperson = slicesofpizza // numberofpeople
perpersonwiththeremainder = slicesofpizza / numberofpeople
remainder = math.ceil(perpersonwiththeremainder - perperson)
print("Each person gets", perperson, "pieces of pizza.")
print("There are", remainder, "leftover pieces.")

# How many people? 8
# How many pizzas do you have? 2
# 8 people with 2 pizzas
# Each person gets 2 pieces of pizza.
# There are 0 leftover pieces.