


#inventory to library
inventory = []

# Function to add to the inventory
def add_item():
    name = input("Enter name: ")
    price = float(input("Enter price: "))
    quantity = int(input("Enter quantity: "))
    category = input("Enter category: ")

#dictionary, categories

    item = {
        'name': name,
        'price': price,
        'quantity': quantity,
        'category': category
    }
#reference to inventory (.append() adds an item to the list
    inventory.append(item)
    print(f"Item '{name}' is added to the inventory.")

#Update Function
def update_item():
    name = input("What to updated: ")
    for item in inventory:
        if item['name'] == name:
            print(f"Updating item: {name}")
            item['price'] = float(input("Enter new price: "))
            item['quantity'] = int(input("Enter new quantity: "))
            item['category'] = input("Enter new category: ")
            print(f"Item '{name}' updated.")
            return
    print(f"Item '{name}' not found. ")

#View Function

def view_inventory():
    if not inventory:
        print("Error. ")
        return
    print("\nInventory:")
    print("{:<10} {:<10} {:<10} {:<10}".format('Name', 'Price', 'Quantity', 'Category'))
    for item in inventory:
        print("{:<10} {:<10} {:<10} {:<10}".format(item['name'], item['price'], item['quantity'], item['category']))
    print()

# remove item
def remove_item():
    name = input("item to be removed: ")
    for item in inventory:
        if item['name'] == name:
            inventory.remove(item)
            print(f"Item '{name}' removed from inventory.")
            return
    print(f"Item '{name}' is not in the inventory.")

#search Items
def search_by_category():
    category = input("Enter category: ")
    found = False
    print(f"Items in category '{category}':")
    print("{:<10} {:<10} {:<10} {:<10}".format('Name', 'Price', 'Quantity', 'Category'))
    for item in inventory:
        if item['category'].lower() == category.lower():
            found = True
            print("{:<10} {:<10} {:<10} {:<10}".format(item['name'], item['price'], item['quantity'], item['category']))
    if not found:
        print(f"No items found '{category}'.")
    print()

# Interaction
while True:
    print("\nMarket Inventory Management System")
    print("1. Add Items")
    print("2. Update Items")
    print("3. View Inventory")
    print("4. Remove Items")
    print("5. Search by Category")
    print("6. Exit")

    choice = input("Enter (1-6): ")

    if choice == '1':
        add_item()
    elif choice == '2':
        update_item()
    elif choice == '3':
        view_inventory()
    elif choice == '4':
        remove_item()
    elif choice == '5':
        search_by_category()
    elif choice == '6':
        print("Close the Inventory")
        break
    else:
        raise ValueError ("Numbers must be from the list.")