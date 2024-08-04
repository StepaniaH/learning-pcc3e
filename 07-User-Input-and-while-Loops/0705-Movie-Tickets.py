prompt = "\nHow old are you? "
prompt += "\n(Enter 'quit' to stop)"

while True:
    age = input(prompt)
    if age == "quit":
        break
    else:
        age = int(age)
        if age < 3:
            print("Charge free!")
        elif 3 <= age < 12:
            print("You'll pay $10.")
        else:
            print("You'll pay $15.")
