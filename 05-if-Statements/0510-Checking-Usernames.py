current_users = ['Admin', 'user1', 'user2', 'user3', 'user4']
new_users = ['admin', 'user1', 'user7', 'user8', 'user9']
current_users = [user.lower() for user in current_users]

for new_user in new_users:
    if new_user.lower() in current_users:
        print("You need to change your username!")
    else:
        print("This is a new user!")
