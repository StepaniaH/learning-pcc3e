prompt = "If you could visit one place in the world, where would you go?"
prompt += "\n(Type 'quit' to exit.)"
location = []
while True:
    user_input = input(prompt)
    if user_input == "quit":
        break
    else:
        location.append(user_input)


print(f"You visited {location}")
