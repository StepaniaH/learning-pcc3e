from pathlib import Path
import json


def get_stored_user_info(path):
    """Get stored user information if available."""
    if path.exists():
        contents = path.read_text()
        user_info = json.loads(contents)
        return user_info
    else:
        return None


def get_new_user(path):
    """Prompt for a new user's information."""
    user_info = {}
    user_info['username'] = input("What is your name? ")
    user_info['birthday'] = input("What is your birthday? ")
    user_info['location'] = input("Where are you from? ")
    contents = json.dumps(user_info)
    path.write_text(contents)
    return user_info


def confirm_user_info(user_info):
    """Confirm if the stored user information is correct."""
    print(f"Is this information correct?")
    print(f"Name: {user_info['username']}")
    print(f"Birthday: {user_info['birthday']}")
    print(f"Location: {user_info['location']}")
    return input("Please enter 'yes' or 'no': ").lower() == 'yes'


def greet_user():
    """Greet the user by name and show their info."""
    path = Path('user_info.json')
    user_info = get_stored_user_info(path)
    if user_info and confirm_user_info(user_info):
        print(f"Welcome back, {user_info['username']}!")
        print(f"You were born on {user_info['birthday']} and live in {
              user_info['location']}.")
    else:
        user_info = get_new_user(path)
        print(f"We'll remember you when you come back, {
              user_info['username']}!")


greet_user()
