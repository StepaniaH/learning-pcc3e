sandwich_orders = ["sd1", "pastrami", "sd2",
                   "sd3", "pastrami", "sd4", "sd5", "pastrami"]
finished_sandwiches = []

print("Sorry, we don't have pastrami.")

while sandwich_orders:
    if sandwich_orders[0] == "pastrami":
        sandwich_orders.pop(0)
    else:
        finished_sandwiches.append(sandwich_orders.pop(0))


print(finished_sandwiches)
