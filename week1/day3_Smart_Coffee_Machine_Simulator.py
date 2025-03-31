# Smart Coffee Machine Simulator
# Author: Simon Lintu
# Date: Week 1, Day 3
# Description: This program simulates the functionality of a smart coffee machine, 
# allowing users to select coffee types, customize their drinks, and manage machine operations.

def main():
    print("Welcome to the Smart Coffee Machine Simulator!")
    print("Brew your perfect cup of coffee with ease.")
    print("------------------------------------------------")

print("Here is a selction of all the coffee types available:")
print("1. Espresso")
print("2. Americano")
print("3. Cappuccino")
print("4. Latte")
print("5. Mocha")
print("6. Flat White")
print("7. Macchiato")
print("8. Cortado")
print("9. Irish Coffee")
print("10. Affogato")

Coffee = input("Select a coffee type by entering the corresponding number (1-10): ")
if Coffee == "1":
    print("You have selected Espresso. That will be $2.50.")
    price = 2.50
elif Coffee == "2":
    print("You have selected Americano. That will be $3.00.")
    price = 3.00
elif Coffee == "3":
    print("You have selected Cappuccino. That will be $3.50.")
    price = 3.50
elif Coffee == "4":
    print("You have selected Latte. That will be $3.75.")
    price = 3.75
elif Coffee == "5":
    print("You have selected Mocha. That will be $4.00.")
    price = 4.00
elif Coffee == "6":
    print("You have selected Flat White. That will be $4.25.")
    price = 4.25
elif Coffee == "7":
    print("You have selected Macchiato. That will be $4.50.")
    price = 4.50
elif Coffee == "8":
    print("You have selected Cortado. That will be $4.75.")
    price = 4.75
elif Coffee == "9":
    print("You have selected Irish Coffee. That will be $5.00.")
    price = 5.00
elif Coffee == "10":
    print("You have selected Affogato. That will be $5.50.")
    price = 5.50
else:
    print("Invalid selection. Please enter a number between 1 and 10.")
print("------------------------------------------------")
Money = input("Please insert money to pay for your coffee: ")
if float(Money) >= price:
    print("Thank you for your payment. Enjoy your coffee!")
    change = float(Money) - price
    print("Your change is: $", change)
else:
    print("Insufficient funds. Please insert more money.")
print("------------------------------------------------")
print("your coffee is being prepared. Please wait a moment.")
print("------------------------------------------------")
print("Your coffee is ready! Enjoy!")
print("------------------------------------------------")
print("Would you like to add a shot with your coffee?")
print("1. Whiskey")
print("2. Vodka")
print("3. No shot")
print("------------------------------------------------")
# Shot selection
menu = {
    "1": ("Whiskey", 2.50),
    "2": ("Vodka", 3.00),
    "3": ("No shot", 0.00),
}
Selection = input("Select a shot type by entering the corresponding number (1-3): ")
if Selection in menu:
    shot_name, shot_price = menu[Selection]
    print(f"You have selected {shot_name}. That will be an additional ${shot_price:.2f}.")
    total_price = price + shot_price
    print(f"Your total is now: ${total_price:.2f}")
else:
    print("Invalid selection. Please enter a number between 1 and 3.")
Money = input("Please insert money to pay for your coffee: ")
if float(Money) >= price:
    print("Thank you for your payment. Enjoy your coffee!")
    change = float(Money) - price
    print("Your change is: $", change)
else:
    print("Insufficient funds. Please insert more money.")
print("------------------------------------------------")
print("have a nice day!")
print("------------------------------------------------")
print("Thank you for using the Smart Coffee Machine Simulator.")
main()