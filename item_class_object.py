class item:
    def __init__(self,n,p,q):
        self.name=n
        self.price=p
        self.quantity=q
    def purchase(self):
        n=int(input("enter the quantity purchased by the customer: "))
        self.quantity=self.quantity-n
    def increasedStock(self):
        n=int(input("enter the quantity that has arrived: "))
        self.quantity=self.quantity+n
    def Display(self):
        print("Name of the item: ",self.name)
        print("Price: ",self.price)
        print("Quantity: ",self.quantity)
        
ob=item('Jeans',1200,30)
ob.purchase()
ob.increasedStock()
ob.Display()

    
