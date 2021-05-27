from product import Product
from order import Order

class Customer:
    def __init__(self):
        self.id_customer = ""
        self.name_customer = ""
        self.orders_customer = []

    def get_order_count(self):
        return int(len(self.orders_customer))

    def get_total(self):
        add = 0
        i = 0
        while i < self.get_order_count():
            add += self.orders_customer[i].get_total()
            i += 1
        return add

    def add_order(self,order):
        self.orders_customer.append(order)

    def display_summary(self):
        print("Summary for customer '{}':".format(self.id_customer))
        print("Name: {}".format(self.name_customer))
        print("Orders: {}".format(self.get_order_count()))
        print("Total: ${:.2f}".format(self.get_total()))

    def display_receipts(self):
        print("Detailed receipts for customer '{}':".format(self.id_customer))
        print("Name: {}".format(self.name_customer))
        print()
        for d in range(0, self.get_order_count()):
            if(d>0):
                print("")
            self.orders_customer[d].display_receipt()