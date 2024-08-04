from user import User
from privileges import Privileges, Admin

new_admin = Admin("John", "Doe", 35, "New York", "john@example.com")
new_admin.privileges.show_privileges()
