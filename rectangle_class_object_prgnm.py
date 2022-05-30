class rectangle:
    
    def get_data(self,l,b):
        self.length=l
        self.breadth=b
        
    def area(self):
        self.area=self.length*self.breadth
        
    def print_data(self):
        print("area is ",self.area)
        
r1=rectangle()
r1.get_data(10,5)
r1.area()
r1.print_data()

r2=rectangle()
r2.get_data(3,4)
r2.area()
r2.print_data()












    
    
