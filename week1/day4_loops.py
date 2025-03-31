for i in range(5):
    print("This is loop number", i)
# The above code will print the loop number from 0 to 4

# The following code demonstrates a while loop
customer = ["John", "Jane", "Doe", "Smith", "Emily"]
for customer_name in customer:
    print("Now serving:", customer_name)
# The above code will print the names of the customers in the list  

for i in range(5):
    print("This is loop number", i)
# The above code will print the loop number from 0 to 4

# The following code demonstrates a while loop
coffees = ["Espresso", "Latte", "Cappuccino"]

for coffee in coffees:
    print("Now preparing:", coffee)


attempts = 3
while attempts > 0:
    password = input("Enter password: ")
    if password == "coffee123":
        print("Access granted.")
        break
    else:
        attempts -= 1
        print("Wrong password. Attempts left:", attempts)



password = ""

while password != "secret":
    password = input("Enter the password: ")

print("Access granted.")

while True:
    print("This will go on forever...")
