# list of toppings
toppings = ["pepperoni", "pineapple", "cheese", "sausage", "olives", "anchovies", "mushrooms"]

# list of prices
prices = [2, 6, 1, 3, 2, 7, 2]

# counts how many times £2 slices appear
num_two_pound_slices = prices.count(2)
# print(num_two_pound_slices)

# tells us how long the list of toppings is - how many toppings
num_pizzas = len(toppings)

print(f"We sell {num_pizzas} different kinds of pizza!")

# 2 dimensional list with pizza + prices
pizza_and_prices = [[2, "pepperoni"],
                    [6, "pineapple"],
                    [1, "cheese"],
                    [3, "sausage"],
                    [2, "olives"],
                    [7, "anchovies"],
                    [2, "mushrooms"]]

# sorts the pizza and prices in ascending order
pizza_and_prices.sort()

cheapest_pizza = pizza_and_prices[0]

priciest_pizza = pizza_and_prices[-1]

# removes last value(s) in pizza_and_prices list
pizza_and_prices.pop()

# inserts 2.5 and peppers into position 4 of list pizzas_and_prices
pizza_and_prices.insert(4, [2.5, "peppers"])

# print(pizza_and_prices)

# takes first 3 values in list pizza_and_prices
three_cheapest = pizza_and_prices[:3]
# print(three_cheapest)

try:
    # get user input for number of slices priced at £2
    num_slices_input = input("Enter the number of £2 slices: ")
    num_slices = int(num_slices_input)

    # calculates total cost for the specified number of £2 slices
    total_cost = num_slices * 2
    print(f"The total cost for {num_slices} £2 slices is £{total_cost}.")
except ValueError:
    print("Invalid input. Please enter a valid number of slices.")
