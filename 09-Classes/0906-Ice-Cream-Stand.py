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


class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ["chocolate", "vanilla", "strawberry"]

    def taste_ice_cream(self):
        print(f"The ice cream stand is serving ice cream in {self.flavors}.")


iceCreamStand = IceCreamStand("The Ice Cream Stand", "American")
iceCreamStand.taste_ice_cream()
