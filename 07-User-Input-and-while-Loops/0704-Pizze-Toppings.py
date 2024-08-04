prompt = "\nWhat toppings would you like on your pizza? "
prompt += "\n(Enter 'quit' to stop)"

while True:
    topping = input(prompt)
    if topping == "quit":
        break
    print(f"You chose {topping}.")
