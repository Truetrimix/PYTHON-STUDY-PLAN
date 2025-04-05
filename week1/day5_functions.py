#This is to make functions flexible
def greet():
    print("Welcome to Python Café!")




# This is to make functions flexible

    print("Hello", name)
greet("John")
greet("Jane")
greet("Doe")

# This is to make functions flexible
def add(a, b):
    return a + b

result = add(3, 5)
print(result)  # 8

# This is to make functions flexible
def make_coffee(drink, cost):
    print(f"Brewing your {drink}...")
    print(f"That will be ${cost:.2f}")

make_coffee("Latte", 3.75)
make_coffee("Espresso", 2.50)

def lynx_settings(mode, speedlimit):
    print(f"Mode - {mode}...")
    print(f"Speed limit {speedlimit:} km/h")

lynx_settings("Full throtle!", 200)
lynx_settings("Normal", 50)

rider = input("Enter your name: ")
def rider():
    print("Are you raeady to blast!?", rider)
    print("_____________________________")


modes = ["Normal", "Full throttle"]
print("Choose your mode:")
for i, mode in enumerate(modes):
    print(f"{i + 1}. {mode}")
choice = int(input("Enter your choice (1 or 2): "))
if choice == 1:
    lynx_settings("Normal", 50)
elif choice == 2:
    lynx_settings("Full throttle!", 200)
else:
    print("Invalid choice. Please select either 1 or 2.")

def main():
    greet("Simon")
    make_coffee("Latte", 3.75)

if __name__ == "__main__":
    main()

