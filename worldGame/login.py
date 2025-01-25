#login app

username = input("Enter your username: ")
password = input("Enter your password: ")

if username == "Irfan" and password == "1234":
    print("Login successful")
elif username != "Irfan" and password == "1234":
    print("Wrong username!")
elif username == "Irfan" and password != "1234":
    print("Wrong password!")
elif username != "Irfan" and password != "1234":
    print("Wrong username and password!")
else:
    print("Login failed")