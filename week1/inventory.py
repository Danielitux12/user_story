#Show the welcome message to the user#
print("Welcome to inventory")
# Function to validate the product name#
def valid_product():
    # Use a global variable to store the product name#
    global product
     # Ask the user to enter the product name#
    product = str(input("Enter name of the product: "))
    # Check if the product name contains only letters#
    if product.isalpha():
        print("PRODUCT VALID :>")
        # Return the valid product name#
        return product
    else:
        print("Write a only name :)")
        # Call the function again if invalid#
        valid_product()
# Function to validate the product price#
def valid_price():
    try:
        # Use a global variable to store the price#
        global price
        # Ask the user to enter the price#
        price = int (input("Enter price of the product: "))
        # Check if the price is greater than 0#
        if price > 0:
            print("PRICE VALID :)")
        else:
            print("This price is negative :( ")
             # Call the function again if invalid#
            valid_price()
    # Handle the case where the input is not a number#
    except ValueError:
        print("Error, invalid price, try again :(")
        # Call the function again if invalid#
        valid_price()
# Function to validate the product quantity#
def valid_quantity():
    try:
        # Use a global variable to store the quantity#
        global quantity
        # Ask the user to enter the quantity#
        quantity = int (input("Enter quantity of the product: "))
        # Check if the quantity is greater than 0#
        if quantity > 0:
            print("QUANTITY VALID :D")
        else:
            print("This quantity is invalid :(")
            # Call the function again if invalid#
            valid_quantity()
    # Handle the case where the input is not a number#
    except ValueError:
        print("Error, invalid quantity, try again :)")
        # Call the function again if invalid#
        valid_quantity()
# Call the functions to get valid data from the user#
valid_product()
valid_price()
valid_quantity()
# Calculate the total cost (price multiplied by quantity)#
total_cost = price * quantity
# Print the total cost of the price and quantity#
print("---INVENTORY---")
# Show the product name#
print(f"Product: {product}")
# Show the price#
print(f"Price: {price}")
# Show the quantity#
print(f"Quantity: {quantity}")
# Show total cost#
print(f"Total cost: {price} x {quantity} = {total_cost}")