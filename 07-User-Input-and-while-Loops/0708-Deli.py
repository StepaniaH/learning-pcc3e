sandwich_orders = ["sd1", "sd2", "sd3", "sd4", "sd5"]
finished_sandwiches = []

for sandwich in sandwich_orders:
    print(f"I made your {sandwich}.")
    made_sandwich = sandwich_orders.pop(0)
    finished_sandwiches.append(made_sandwich)

print(f"Here are your finished sandwiches: {finished_sandwiches}")
