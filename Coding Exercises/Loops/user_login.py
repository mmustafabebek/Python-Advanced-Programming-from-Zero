print("""
**************************
User Login Program
**************************
""")

sys_user_name = "mmustafa"

sys_password = "12345"
rightofentry = 3


while True:
    user_name = input("User Name:")
    password = input("Password:")
    if(user_name != sys_user_name and password == sys_password):
        print("Username Incorrect...")
        rightofentry -= 1
    elif(user_name == sys_user_name and password != sys_password):
        print("Password Incorrect...")
        rightofentry -= 1
    elif (user_name!= sys_user_name and password != sys_password):
        print("Username and Password Incorrect...")
        rightofentry -= 1
    else:
        print("Login to the System Successfully...")
        break
    if(rightofentry == 0):
        print("Your Entry Right Has Expired...")
        break