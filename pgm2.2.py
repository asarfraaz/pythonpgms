svalue=input("what is the starting value of odometer?")
svalue=int(svalue)
evalue=input("what is the end value of odometer?")
evalue=int(evalue)
fuel=input("how much fuel used?")
fuel=int(fuel)
tankcap=input("what is the tank capacity of the car?")
tankcap=int(tankcap)
mil=(evalue-svalue)/fuel
print("mileage is ",mil)
totdis=mil*tankcap
count=0
distrav=560
while(distrav>totdis ):
    count=count+1
    distrav=distrav-totdis
print("the no of stops req is",count)    
    
    
