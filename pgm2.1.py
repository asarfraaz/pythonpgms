svalue=input("what is the starting value of odometer?")
svalue=int(svalue)
evalue=input("what is the end value of odometer?")
evalue=int(evalue)
fuel=input("how much fuel used?")
fuel=int(fuel)
mil=(evalue-svalue)/fuel
print("mileage is ",mil)
