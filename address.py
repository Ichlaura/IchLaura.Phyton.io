
class Address:
    def __init__(self):
        self.street = ""
        self.city = ""
        self.state = ""
        self.zip = ""

    def display1(self):
        print(self.street)
        print("{}, {} {}".format(self.city, self.state, self.zip))
    