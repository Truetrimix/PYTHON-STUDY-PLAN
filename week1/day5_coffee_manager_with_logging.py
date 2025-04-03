# Coffee Order Manager with Logging
from datetime import datetime

def greet():
    print("Welcome to Simulation Café!")

def menu():
    print("1. Latte, $3.75")
    print("2. Espresso, $2.50")
    print("3. Cappuccino, $4.00")
    print("4. Mocha, $3.50")
    print("5. Americano, $2.75")
    print("6. Macchiato, $3.25")
    print("7. Flat White, $4.50")

def get_order():
    order = input("Enter the number of your choice: ")
    return order

def get_payment():
    try:
        payment = float(input("Enter your payment amount: "))
        return payment
    except ValueError:
        print("Invalid input. Please enter a number.")
        return 0

def process_order(order):
    drinks = {
        "1": ("Latte", 3.75),
        "2": ("Espresso", 2.50),
        "3": ("Cappuccino", 4.00),
        "4": ("Mocha", 3.50),
        "5": ("Americano", 2.75),
        "6": ("Macchiato", 3.25),
        "7": ("Flat White", 4.50)
    }
    if order in drinks:
        name, price = drinks[order]
        print(f"You ordered a {name}.")
        return name, price
    else:
        print("Invalid choice. Please select a valid drink number.")
        return None, 0

def check_payment(order_cost, payment):
    if payment >= order_cost:
        change = payment - order_cost
        print(f"Thank you for your purchase! Your change is ${change:.2f}.")
        return True
    else:
        print("Insufficient payment. Please try again.")
        return False

def log_order(drink_name, cost, payment):
    with open("order_log.txt", "a") as file:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"{timestamp} - Ordered: {drink_name} | Cost: ${cost:.2f} | Paid: ${payment:.2f}\n")

def main():
    greet()
    print("Please select a drink from the menu:")
    print("-----------------------")
    menu()
    order = get_order()
    drink_name, order_cost = process_order(order)
    if order_cost > 0:
        payment = get_payment()
        if check_payment(order_cost, payment):
            log_order(drink_name, order_cost, payment)
    else:
        print("Order not processed due to invalid choice.")

if __name__ == "__main__":
    main()
