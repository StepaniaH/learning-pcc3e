pizzas = ['Neapolitan Pizza', 'New York-Style Pizza',
          'Chicago-Style Deep-Dish Pizza', 'California-Style Pizza', 'Sicilian-Style Pizza']

pizza = 'Neapolitan Pizza'
# test 1
print("\nIs pizza == 'Neapolitan Pizza'? I predict Ture.")
print(pizza == 'Neapolitan Pizza')

# test 2
print("\nIs pizza != 'Neapolitan Pizza'? I predict False.")
print(pizza != 'Neapolitan Pizza')

# test 3
print("\nIs pizza in pizzas? I predict True.")
print(pizza in pizzas)

# test 4
print("\nIs pizza not in pizzas? I predict False.")
print(pizza not in pizzas)

one = 1
two = 2
three = 3
# test 5
print("\nIs one bigger than two? I predict False.")
print(one > two)

# test 6
print("\nIs one smaller than two? I predict True.")
print(one < two)

# test 7
print("\nIs one bigger than two and two smaller than three? I predict False.")
print(one > two and two < three)

# test 8
print("\nIs one bigger than two or two smaller than three? I predict True.")
print(one > two or two < three)

# test 9
print("\nIs one smaller than two or two smaller than three? I predict True.")
print(one < two or two < three)

# test 10
print("\nIs one smaller than two and two smaller than three? I predict True.")
print(one < two and two < three)
