class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"The restaurant is called {
              self.restaurant_name} and serves {self.cuisine_type} food.")

    def open_restaurant(self):
        print(f"The restaurant is open.")


restaurant = Restaurant("The Cheesecake Factory", "American")
restaurant.describe_restaurant()
restaurant.open_restaurant()
