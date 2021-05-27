
class Product:
    def __init__(self,id,name,price,quantity):
        self.id_product = id
        self.name_product = name
        self.price_product = price
        self.quantity_product = quantity

    def get_total_price(self):
        total_price = self.price_product * self.quantity_product
        return total_price

    def display1(self):
        self.get_total_price()
        print("{} ({}) - ${:.2f}".format(self.name_product, self.quantity_product,self.get_total_price()))