class User:
    def __init__(self, first_name, last_name, age, location, email):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.location = location
        self.email = email

    def describe_user(self):
        print(f"The user is called {self.first_name} {
              self.last_name} and is {self.age} years old.")
        print(f"They live in {
              self.location} and have the email address {self.email}.")

    def greet_user(self):
        print(f"Hello, {self.first_name}!")


user_1 = User("John", "Smith", 25, "New York", "john@smith.com")
user_1.describe_user()
user_1.greet_user()
print("\n")

user_2 = User("Jane", "Doe", 30, "Los Angeles", "jane@doe.com")
user_2.describe_user()
user_2.greet_user()
