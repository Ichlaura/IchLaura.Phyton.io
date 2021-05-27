
from customer import Customer
from order import Order
from product import Product

def main():
    print("### Testing Products ###")
    product1 = Product("1238223", "Sword", 1899.99, 10)

    print("Id: {}".format(product1.id_product))
    print("Name: {}".format(product1.name_product))
    print("Price: {}".format(product1.price_product))
    print("Quantity: {}".format(product1.quantity_product))

    product1.display1()

    print()

    product2 = Product("838ab883", "Shield", 989.75, 6)
    print("Id: {}".format(product2.id_product))
    print("Name: {}".format(product2.name_product))
    print("Price: {}".format(product2.price_product))
    print("Quantity: {}".format(product2.quantity_product))

    product2.display1()

    print("\n### Testing Orders ###")
    # Now test Orders
    order1 = Order()
    order1.id_order = " 1138"
    order1.add_product(product1)
    order1.add_product(product2)

    order1.display_receipt()

    print("\n### Testing Customers ###")
    # Now test customers
    customer1 = Customer()
    customer1.id_customer = "aa32"
    customer1.name_customer = "Gandalf"
    customer1.add_order(order1)

    customer1.display_summary()
    print()
    customer1.display_receipts()

    # Add another product and order and display again

    product3 = Product("2387127", "The Ring", 1000000, 1)
    product4 = Product("1828191", "Wizard Staff", 199.99, 3)

    order2 = Order()
    order2.id_order = " 1277182"
    order2.add_product(product3)
    order2.add_product(product4)

    customer1.add_order(order2)
    print()
    customer1.display_summary()
    print()
    customer1.display_receipts()


if __name__ == "__main__":
    main()