#This is a simple coffee manager program
def greet():
    print("Welcome to Simulation Café!")
greet()

def menu():
    print("1. Latte, $3.75")
    print("2. Espresso, $2.50")
    print("3. Cappuccino, $4.00")
    print("4. Mocha, $3.50")
    print("5. Americano, $2.75")
    print("6. Macchiato, $3.25")
    print("7. Flat White, $4.50")

print("Please select a drink from the menu:")
print("-----------------------")
menu()

def get_order():
    order = input("Enter the number of your choice: ")
    return order
def get_payment():
    payment = float(input("Enter your payment amount: "))
    return payment
def process_order(order):
    if order == "1":
        print("You ordered a Latte.")
        return 3.75
    elif order == "2":
        print("You ordered an Espresso.")
        return 2.50
    elif order == "3":
        print("You ordered a Cappuccino.")
        return 4.00
    elif order == "4":
        print("You ordered a Mocha.")
        return 3.50
    elif order == "5":
        print("You ordered an Americano.")
        return 2.75
    elif order == "6":
        print("You ordered a Macchiato.")
        return 3.25
    elif order == "7":
        print("You ordered a Flat White.")
        return 4.50
    else:
        print("Invalid choice. Please select a valid drink number.")
        return 0
def check_payment(order_cost, payment):
    if payment >= order_cost:
        change = payment - order_cost
        print(f"Thank you for your purchase! Your change is ${change:.2f}.")
    else:
        print("Insufficient payment. Please try again.")
def main():
    order = get_order()
    order_cost = process_order(order)
    if order_cost > 0:
        payment = get_payment()
        check_payment(order_cost, payment)
    else:
        print("Order not processed due to invalid choice.")
from datetime import datetime

if __name__ == "__main__":

    def log_order(drink_name, cost, payment):
        with open("order_log.txt", "a") as file:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            file.write(f"{timestamp} - Ordered: {drink_name} | Cost: ${cost:.2f} | Paid: ${payment:.2f}\n")    

main()



# This is a simple coffee manager program