class User:
    def __init__(self, first_name, last_name, age, location, email):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.location = location
        self.email = email
        self.login_attempts = 0

    def describe_user(self):
        print(f"The user is called {self.first_name} {
              self.last_name} and is {self.age} years old.")
        print(f"They live in {
              self.location} and have the email address {self.email}.")

    def greet_user(self):
        print(f"Hello, {self.first_name}!")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0


user = User("John", "Smith", 25, "New York", "john@smith.com")

print(f"You have tried {user.login_attempts} times.")
user.increment_login_attempts()
print(f"You have tried {user.login_attempts} times.")
user.reset_login_attempts()
print(f"You have tried {user.login_attempts} times.")
