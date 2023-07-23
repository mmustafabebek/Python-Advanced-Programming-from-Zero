print("""************************************
User Login
************************************
""")

sys_user_name = "mmustafa"
password = "12345"

user_name = input("Your User Name:")
user_password = input("Your Password:")

if (user_name == sys_user_name and user_password != password):
    print("Password Incorrect...")
elif (user_name != sys_user_name and user_password == password):
    print("Username Incorrect...")
elif (user_name != sys_user_name and user_password != password):
    print("Username and Password Incorrect...")
else:
    print("Successfully logged into the system...")
