

from address import Address

class CreditCard:
    def __init__(self):
        self.name = ""
        self.number = ""
        self.mailing = Address()
        self.billing = Address()

    def display(self):
        print(self.name)
        print(self.number)
        
        print("Mailing Address:")
        self.mailing.display1()
        
        print("Billing Address:")
        self.billing.display1()