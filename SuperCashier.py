def add_product():
    enter_detail = True
    while enter_detail:
        detail = input("enter A to continue and Q to quit: ")
        if detail == 'A':
            product = input("enter product: ")
            quantity = int(input("enter quantity: "))
            buying_data.update({product: quantity})
        elif detail == 'Q':
            enter_detail = False
        else:
            print("enter correct information")
    return buying_data

def get_price(product, quantity):
    price_data = {'Biscuit': 3, 'Chicken': 5, 'Egg': 1, 'Fish': 3, 'Coke': 2, 'Bread': 2, 'Apple': 3, 'Onion': 3}
    if product in price_data.keys():
        subtotal = price_data[product]*quantity
        print(f"price of "+product+" is "+"$ "+str(price_data[product])+" * "+str(quantity)+" = "+str(subtotal))
    else:
        print("this product is not available in store")
    return subtotal

def get_discount(billamount, membership):
    discount = 0
    if billamount > 25:
        if membership == 'Gold':
            billamount = 0.80*float(billamount)
            discount = 20
        elif membership == 'Silver':
            billamount = 0.90*float(billamount)
            discount = 10
        elif membership == 'Bronze':
            billamount = 0.95*float(billamount)
            discount = 5
        print(f"{discount} % for {membership} membership and bill is {str(billamount)}")
    else:
        print("there is no discount for bill amount less than $25")
    return billamount


def get_bill(buying_data, membership):
    billamount = 0
    for key, value in buying_data.items():
        billamount += get_price(key, value)
    billamount = get_discount(billamount, membership)
    print("Thank you visit again")

shop = input("Welcome to shop, press E to enter:")
if shop == 'E':
    membership = input("enter membership: ")
    buying_data = {}
    add_product()
    get_bill(buying_data, membership)
else:
    print("Thank you visit again")











