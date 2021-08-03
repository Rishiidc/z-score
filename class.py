class Ps4:
    def __init__(self,type,price,memory,quantity):
        self.type = type
        self.price = price
        self.memory = memory
        self.quantity = quantity
    def enquiry(self):
        print("Price ->"+str(self.price))
        print("Memory ->"+self.memory)
        print("Quantity ->"+str(self.quantity))
        print("PS4 Type ->"+self.type)
    def buy(self):
        if(self.quantity>0):
            self.quantity -= 1 
            print("Congratulations")
        else:
            print("Sorry,sold out")
    def sell(self):
        self.quantity += 1
        print("Thank you for selling")
          
original = Ps4("Original",40000,"500GB",3)
slim1 = Ps4("Slim1",27000,"500GB",3)
slim2 = Ps4("Slim2",32000,"1TB",1)
pro = Ps4("Pro",36000,"1.5TB",0)

slim2.enquiry()
slim1.buy()
pro.buy()
original.sell()