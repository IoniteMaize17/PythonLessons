class delivery:
    """Class defines a delivery package"""
    item = ""
    name =""
    address=""
def addnew():
    customer = input("Customer name: ")
    place = input("Delivery address: ")
    stuff = input("what is the package: ")
    
    packet = delivery()
    packet.item = stuff
    packet.name = customer
    packet.address = place
    return packet
def main():
    round = []
    total = int(input("How many packages?"))
    for i in range(0,total):
        deliver = addnew()
        round.append(deliver)
    
    print("Drop-off places:")
    for i in range(0,total):
        print(round[i].name+":"+round[i].address+":"+round[i].item)

if __name__ == "__main__":
    main()