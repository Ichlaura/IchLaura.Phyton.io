


from credit_card import CreditCard

def main():
    #Crea el objeto desde el archivo de la tarjeta de crédito
    custom1 = CreditCard()
    custom1.name = input("Name: ")
    custom1.number = input("Number: ")
    print("Mailing Address:")
    #llama object.specific atributo para poner,specific atribute.
    custom1.mailing.street = input("Street: ")
    custom1.mailing.city = input("City: ")
    custom1.mailing.state = input("State: ")
    custom1.mailing.zip = input("Zip: ")
    print("Billing Address:")
    #llama object.specific atributo para poner,specific atribute.
    custom1.billing.street = input("Street: ")
    custom1.billing.city = input("City: ")
    custom1.billing.state = input("State: ")
    custom1.billing.zip = input("Zip: ")
    #Llama al método object.call desde el archivo de la tarjeta de crédito
    custom1.display()

if __name__=="__main__":
    main()