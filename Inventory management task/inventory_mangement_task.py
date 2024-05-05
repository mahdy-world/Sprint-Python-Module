# empty list to store inventory items
inventory = []

# function to create new item 
def create_new_item():
    # ask user to enter item  data(name, price, quantity)
    name = input("Enter item name: ").strip().upper()
    price = input("Enter item price: ")
    quantity = input("Enter item quantity: ")
    
    # store data in dictionary 
    item = {"name": name, "price": price, "quantity": quantity}
    # append item dictionary into inventory list
    inventory.append(item)
    # print success message with new item information 
    print(f"Item added successfuly ==> Name: {name} == Price: {price}$ == Quantity: {quantity}")


# function to update stock 
def update_stock():
    # ask user for item name to update it 
    name = input("Enter item name: ").strip().upper()
    # loop through inventory list to get item name that user enter before 
    for item in inventory:
        # check if name from user == name from loop
        if item["name"] == name:
            # ask user to put new quantity
            quantity = input("Enter new quantity: ")
            # update quantity 
            item["quantity"] = quantity
            # get item price and name from loop to print them after update operation success 
            name_obj = item['name']
            price_obj = item['price']
            quantity_obj = item['quantity']
            # print success message with item information
            print(f"Stock Updated Successfuly ==> Name: {name_obj} == Price: {price_obj}$ == Quantity: {quantity_obj}")
            return
    # if item does not exist in invontry list print message that Item not found
    print("Item not found")

# function to generate sales report
def generate_sales_report():
    # set total revenue to 0
    total_revenue = 0
    print("\nSales Report:")
    # loop through invenroty list 
    for item in inventory:
        # get item price and item quantity from loop to multiply them
        revenue = int(item["price"]) * int(item["quantity"])
        # update total_revenue variable to revenue 
        total_revenue += revenue
        # print name, price and quantity for each item
        print(f"{item['name']}: Quantity => {item['quantity']}, Revenue => ${revenue:.2f}")
    # print total revenue
    print(f"\n === ***Total Revenue*** === : ${total_revenue:.2f}")

# function to print popular items
def popular_items():
    # use sorted function to sort the inventory list based on the value of quantity key in ech item dictionary and sorted shoud be done in descending order
    sorted_inventory = sorted(inventory, key=lambda x: x["quantity"], reverse=True)
    # The key parameter specifies a function that will be called on each element of the list to determine its sorting key. 
    # In this case, the lambda function extracts the value of the "quantity" key from each item dictionary (x) in the inventory list.
    # The reverse=True parameter specifies that the sorting should be done in descending order (from largest to smallest).
    print(sorted_inventory)
    print("\n === ***Top 3 Popular Items*** ===:")
    # loop through sorted_inventory and return item name and item quantity and print them 
    for i, item in enumerate(sorted_inventory[:3]):
        print(f"{i+1}. {item['name']} - Quantity: {item['quantity']}")
        
            

def main():
    while True:
        # print main options for system to make user choice form them 
        print("\n === ***Inventory Management System*** ===")
        print("1. Add New Item")
        print("2. Update Stock")
        print("3. Generate Sales Report")
        print("4. Popular Items")
        print("5. Exit")
        choice = input("Enter your choice: ")
        # check user choice and run function based on user choice
        if choice == '1':
            create_new_item()
        elif choice == '2':
            update_stock()
        elif choice == '3':
            generate_sales_report()
        elif choice == '4':
            popular_items()
        elif choice == '5':
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Please try again.")

# Main Program
if __name__ == "__main__":
    main()