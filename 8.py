# №8

import math

number_of_people = int(input("How many people?"))
amount_of_pizza = int(input("How many pizzas do you have?"))

slices_of_pizza = amount_of_pizza * 8  # шматочків піци
perperson = slices_of_pizza // number_of_people
per_person_with_there_mainder = slices_of_pizza / number_of_people
remainder = math.ceil(per_person_with_there_mainder - perperson)

print("Each person gets", perperson, "pieces of pizza.")
print("There are", remainder, "leftover pieces.")

# How many people? 8
# How many pizzas do you have? 2
# 8 people with 2 pizzas
# Each person gets 2 pieces of pizza.
# There are 0 leftover pieces.
