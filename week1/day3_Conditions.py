temperature = 29

if temperature > 20:
    print("It's a warm day!")

temperature = 1590

if temperature > 20:
    print("It's a warm day!")
else:
    print("It's a bit chilly.")

temperature = 70

if temperature > 30:
    print("It's hot.")
elif temperature > 20:
    print("It's warm.")
else:
    print("It's cool.")

username = input("Enter username: ")
password = input("Enter password: ")

if username == "admin" and password == "1234":
    print("Access granted.")
else:
    print("Access denied.")

time = input("What time is it in xx:xx format? ")
day = input("What day is it? ")

if time == "12:00" and day == "Monday":
    print("You have won the lottery!")
else:
    print("you failed")
    
age = input("Enter your age: ")
if int(age) < 18:
    print("You are a minor.")
elif int(age) < 65:
    print("You are an adult.")
else:
    print("You are a senior citizen.")

access = input("Eneter you name to access the sytem: ")
Password = input("Enter your password: ")
if access == "admin" and Password == "1234":
    print("Access granted.")
elif access == "user" and Password == "abcd":
    print("Access granted.")
else:
    print("Access denied. You are not authorized to access this system.")
if access == "admin":
    print("Welcome, admin!")
elif access == "user":
    print("Welcome, user!")
else:
    print("Access denied.")
    
