inventory = []

def menu():
    print("\n""1. enter product.")
    print("2. show inventory.")
    print("3. calculate statistics.")
    print("4. leave.""\n")
    try:
        global option
        option = int (input("Enter your option: "))
        if option in range (1,5):
            print(f"Select option {option}\n")
        else:
            print(f"Dont exist option {option}, try again")
            menu()
    except ValueError:
        print("Error try again and select a valid option")
        menu()
inventory = []
def val_product():
    while True:
        product = str (input("\nEnter product: "))
        if product.isalpha():
            return product
        else:
            print("Enter alphabetical characters only")
def val_price():
    while True:
        try:
            price = int (input("Enter price of the product: "))
            if price > 0:
                return price
            else:
                print("This price is negative")
        except ValueError:
            print("Error, invalid price, try again")
def val_quantity():
    while True:
        try:
            quantity = int (input("Enter quantity of the product: "))
            if quantity > 0:
                return quantity
            else:
                print("This quantity is invalid")
        except ValueError:
            print("Error, invalid quantity, try again")
def show_inventory():
    objects=(len(inventory))
    if objects > 0:
        count = 0
        for i in inventory:
            print(f"{count+1}. Product: {i["product"]} = {i["price"]} - {i["quantity"]}")
            count=+1
    else:
        print("The inventory is empty")
            
while True:
    menu()
    if option == 1:
        product = val_product()
        price = val_price()
        quantity = val_quantity()
        inventory.append({
            "product": product,
            "price": price,
            "quantity": quantity})
    elif option == 2:
        show_inventory()