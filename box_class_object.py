class box:
    def __init__(self,l,b,h):
        self.length=l
        self.breadth=b
        self.heigth=h
    def show_data(self):
        print('length',self.length)
        print('breadth',self.breadth)
        print('heigth',self.heigth)
    def volume(self):
        v=self.length*self.breadth*self.heigth
        print('volume',v)
    def __add__(self,B):
        l=self.length+B.length
        b=self.breadth+B.breadth
        h=self.heigth+B.heigth
        b=box(l,b,h)
        return b
    
b1=box(2,3,4)
b2=box(1,1.2,3.2)
b1.show_data()
b1.volume()
b2.show_data()
b2.volume()
b3=b1+b2    #b1.__add__(b2)
b3.show_data()
b3.volume()
