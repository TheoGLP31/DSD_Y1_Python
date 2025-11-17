# Clinic vaccine stock (single brand for simplicity)
stock = 50

def dispense(doses):
    global stock
    stock = stock - doses
    print("Dispensed:", doses, "Remaining:", stock)

def restock(amount):
    global stock

    print("Before restock:", stock)
    stock = stock + amount
    print("After restock:", stock)

while True:
    dispense(5)
    restock(10)

    print("End of day stock:", stock)