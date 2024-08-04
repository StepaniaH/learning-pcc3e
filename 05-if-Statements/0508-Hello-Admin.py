user_names = ['admin', 'user1', 'user2', 'user3', 'user4']

for user in user_names:
    if user == 'admin':
        print('Hello admin, would you like to see a status report?')
    else:
        print(f"Hello {user}, thank you for logging in again!")
