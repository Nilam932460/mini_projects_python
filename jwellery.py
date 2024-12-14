jewelry_list = [
    {'id': '1', 'name': 'Gold Ring', 'price': '5000', 'category': 'Ring', 'stock': '10'},
    {'id': '2', 'name': 'Diamond Necklace', 'price': '20000', 'category': 'Necklace', 'stock': '5'},
    {'id': '3', 'name': 'Silver Bracelet', 'price': '3000', 'category': 'Bracelet', 'stock': '8'}
]

# Create a menu loop
while True:
    print("Jewelry Management System")
    print("1. Add Item")
    print("2. View Items")
    print("3. Update Item")
    print("4. Delete Item")
    print("5. Exit")
    
    # Get user's choice
    choice = input("Enter your choice (1-6): ")
    
    if choice == "1":  # Add Item
        print("\n--- Add Jewelry Item ---")
        item_id = input("Enter ID: ")
        name = input("Enter Name of item : ")
        price = input("Enter Priceof item : ")
        category = input("Enter Category (e.g., Ring, Necklace): ")
        stock = input("Enter Stock Quantity: ")
        # Add to the jewelry list
        jewelry_list.append({
            "id": item_id,
            "name": name,
            "price": price,
            "category": category,
            "stock": stock
        })
        print("Item added successfully!")
    
    elif choice == "2":  # View Items
        print("\n--- Jewelry Items ---")
        if not jewelry_list:
            print("No items to display.")
        else:
            for item in jewelry_list:
                print(f"ID: {item['id']}, Name: {item['name']}, Price: {item['price']}, Category: {item['category']}, Stock: {item['stock']}")
    
    elif choice == "3":  # Update Item
        print("\n--- Update Jewelry Item ---")
        update_id = input("Enter the ID of the item to update: ")
        for item in jewelry_list:
            if item['id'] == update_id:
                print(f"Current Details: {item}")
                item['name'] = input("Enter New Name of item: ") or item['name']
                item['price'] = input("Enter New Price of item: ") or item['price']
                item['category'] = input("Enter New Category: ") or item['category']
                item['stock'] = input("Enter New Stock: ") or item['stock']
                print("Item updated successfully!")
                break
        else:
            print("Item not found!")
    
    elif choice == "4":  # Delete Item
        print("\n--- Delete Jewelry Item ---")
        delete_id = input("Enter the ID of the item to delete: ")
        for item in jewelry_list:
            if item['id'] == delete_id:
                jewelry_list.remove(item)
                print("Item deleted successfully!")
                break
        else:
            print("Item not found!")
    
    
    elif choice == "5":  # Exit
        print("Exiting... Goodbye!")
        break
    
    else:  # Invalid Input
        print("Invalid choice! Please enter a number between 1 and 6.")

