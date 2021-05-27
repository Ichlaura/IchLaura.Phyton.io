from product import Product

class Order:
    def __init__(self):
        self.id_order = " "
        self.products_order = []

    def get_subtotal(self):
        total = 0
        for p in self.products_order:
            total = total + p.get_total_price()
        return total

    def get_tax(self):
        tax = self.get_subtotal() * 0.065
        return tax

    def get_total(self):
        total = self.get_subtotal() + self.get_tax()
        return total

    def add_product(self, product):
        self.products_order.append(product)

    def display_receipt(self):
        print("Order:{}" .format(self.id_order))
        for p in self.products_order:
            p.display1()
        print("Subtotal: ${:.2f}".format(self.get_subtotal()))
        print("Tax: ${:.2f}".format(self.get_tax()))
        print("Total: ${:.2f}".format(self.get_total()))