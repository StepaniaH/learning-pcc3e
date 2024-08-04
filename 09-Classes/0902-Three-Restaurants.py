class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"The restaurant is called {
              self.restaurant_name} and serves {self.cuisine_type} food.")

    def open_restaurant(self):
        print(f"The restaurant is open.")


restaurant_1 = Restaurant("The Cheesecake Factory", "American")
restaurant_1.describe_restaurant()
restaurant_1.open_restaurant()
print("\n")

restaurant_2 = Restaurant("The Pizza Place", "Italian")
restaurant_2.describe_restaurant()
restaurant_2.open_restaurant()
print("\n")

restaurant_3 = Restaurant("The Burger Joint", "American")
restaurant_3.describe_restaurant()
restaurant_3.open_restaurant()
print("\n")
