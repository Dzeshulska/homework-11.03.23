user_email = input("Enter your email :")
x = "@"
y = "."
if x and y in user_email:
   pass
else:
    print("Error")


user_login = input("Enter your login :")
a = "@"
b = "!"
if a and b in user_login and len(user_login) > 6 :
   print(user_login)
else:
   print("Error")       


user_password = input("Enter your password :")
print(user_password)


user_name = input("Enter your name :")
if len(user_name) >= 2 :
   print(user_name.capitalize())
else:
   print("Error")