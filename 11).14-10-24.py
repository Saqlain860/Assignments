# Encapsulation

# encapsulation is the process of cobining attributes and methods within the class.
#it prevents outer classes from accesing and chanfing attributes and methods of a class.This helps to achive data hiding

class Computer:
    def __init__(self):
        self.__maxprice = 1000 #private attribute
    
    def sell(self):
        print(f"selling price : {self.__maxprice}")
    
    def setMaxprice(self,price):
        self.__maxprice = price

c = Computer()
c.sell()
c.setMaxprice(12000)
c.sell()