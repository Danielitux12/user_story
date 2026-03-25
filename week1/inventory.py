print("Welcome to inventory")
def valid_product():
    product = str(input("Enter name of the product: "))
    if product == "":
        print("Enter a valid product")
        valid_product()
def valid_price():
    try:
        price = float (input("Enter price of the product: "))
        if price > 0:
            print("PRICE VALID :)")
        else:
            print("This price is negative :( ")
            valid_price()
    except ValueError:
        print("Error, invalid price, try again :(")
        valid_price()
def valid_quantity():
    try:
        quantity = int (input("Enter quantity of the product: "))
        if quantity > 0:
            print("QUANTITY VALID :D")
        else:
            print("This quantity is invalid :(")
            valid_quantity()
    except ValueError:
        print("Error, invalid quantity, try again :)")
        valid_quantity()