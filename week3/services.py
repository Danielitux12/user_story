from validations import val_product
from validations import val_price
from validations import val_quantity

product = val_product()
price = val_price()
quantity = val_quantity()

inventory = [{
    "product": product,
    "price": price,
    "quantity": quantity
}]

def show_inventory():
    for i in inventory:
        print(f"Product: {i["product"]} = {i["price"]} - {i["quantity"]}")

def search_product():
    