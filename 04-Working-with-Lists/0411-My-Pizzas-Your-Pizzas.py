pizzas = ['Neapolitan Pizza', 'New York-Style Pizza',
          'Chicago-Style Deep-Dish Pizza', 'California-Style Pizza', 'Sicilian-Style Pizza']

friend_pizza = pizzas[:]

pizzas.append('Tokyo-Style Pizza')
friend_pizza.append('Cypriot-Style Pizza')

print("My favorite pizzas are:")
for my in pizzas:
    print(my)

print("\nMy friend's favorite pizzas are:")
for friend in friend_pizza:
    print(friend)
