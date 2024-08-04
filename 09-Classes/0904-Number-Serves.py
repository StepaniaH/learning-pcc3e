class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"The restaurant is called {
              self.restaurant_name} and serves {self.cuisine_type} food.")

    def open_restaurant(self):
        print(f"The restaurant is open.")

    def set_number_served(self, number_served):
        self.number_served = number_served
        print(f"The restaurant has been served {self.number_served} times.")

    def increment_number_served(self, number_served):
        self.number_served += number_served
        print(f"The restaurant has been served {self.number_served} times.")


restaurant = Restaurant("The Cheesecake Factory", "American")
restaurant.describe_restaurant()
restaurant.open_restaurant()

restaurant.set_number_served(10)
restaurant.increment_number_served(5)
