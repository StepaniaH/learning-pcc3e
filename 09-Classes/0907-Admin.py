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


class Admin(User):
    def __init__(self, first_name, last_name, age, location, email):
        super().__init__(first_name, last_name, age, location, email)
        self.privileges = ["can add post", "can delete post", "can ban user"]

    def show_privileges(self):
        print(f"The admin has the following privileges: {self.privileges}.")


admin = Admin("John", "Smith", 25, "New York", "john@smith.com")

admin.show_privileges()
