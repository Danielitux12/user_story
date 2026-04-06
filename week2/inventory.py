def val_option ():
    while True:
        try:
            option = int (input("Enter your option: "))
            if option in range (1,5):
                print(f"Select option {option}\n")
                return option
            else:
                print(f"Don't exist option {option}, try again")
        except ValueError:
            print("Error try again and select a valid option")

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

inventory = []
           
def enter_product():
    product = val_product()
    price = val_price()
    quantity = val_quantity()
    inventory.append({
        "product": product,
        "price": price,
        "quantity": quantity})

def show_inventory():
    objects=(len(inventory))
    if objects > 0:
        count = 0
        for i in inventory:
            print(f"{count+1}. Product: {i["product"]} = {i["price"]} - {i["quantity"]}")
            count=+1
    else:
        print("The inventory is empty")

def calculate_statistics():
    objects=(len(inventory))
    if objects > 0:
        count = 0
        for i in inventory:
            print(f"{count+1}. Product: {i["product"]} = {i["price"]*i["quantity"]}")
            count=+1
    else:
        print("The inventory is empty")

def show_options():
    print("\n""1. enter product.")
    print("2. show inventory.")
    print("3. calculate statistics.")
    print("4. leave.""\n")
    
def menu ():
    while True:
        show_options()
        option = val_option()
        if option == 1:
            enter_product()
        elif option == 2:
            show_inventory()
        elif option == 3:
            calculate_statistics()
        elif option == 4:
            print("Thanks for use the program")
            break
menu()