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
            