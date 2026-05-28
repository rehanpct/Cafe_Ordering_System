# Menu items
menu = {
    1: {"name": "Coffee", "price": 20},
    2: {"name": "Tea", "price": 15},
    3: {"name": "Sandwich", "price": 50},
    4: {"name": "Pasta", "price": 200},
    5: {"name": "Burger", "price": 150}
}

# Display the menu
print("Welcome to the Cafe!")
print("Here is the menu:")
print("----------------------------")
for id, item in menu.items():
    print(id, ".", item["name"], "-", "₹", item["price"])
print("----------------------------")

# Taking orders
orders = []
total = 0

while True:
    try:
        id = int(input("Enter the item number to order (or 0 to finish): "))
        if id == 0:
            break
        if id in menu:
            qty = int(input("How many " + menu[id]["name"] + "? "))
            total += menu[id]["price"] * qty
            orders.append({"name": menu[id]["name"], "qty": qty, "price": menu[id]["price"]})
            print("Added", qty, menu[id]["name"] + "(s) to your order.")
        else:
            print("Invalid item number. Please try again.")

    except ValueError:
        print("Invalid item number. Please try again.") 

# Printing the receipt
print("\nOrder Receipt")
print("----------------------------")
for order in orders:
    print(order["qty"], "x", order["name"], "-", "₹", order["qty"] * order["price"])
print("----------------------------")
print("Total Amount: ₹", total)
print("Thank you for visiting!")