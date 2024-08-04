pizzas = ['Neapolitan Pizza', 'New York-Style Pizza',
          'Chicago-Style Deep-Dish Pizza', 'California-Style Pizza', 'Sicilian-Style Pizza']

print("The first three items in the list are:")
for i in pizzas[:3]:
    print(i)

print("\nThree items from the middle of the list are:")
for i in pizzas[1:4]:
    print(i)

print("\nThe last three items in the list are:")
for i in pizzas[-3:]:
    print(i)
