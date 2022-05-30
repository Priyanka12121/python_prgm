class a:
    def __init__(self,ncl):
        self.name=n
    #def show(self):
        #print('name:',self.name)
class b(a):
    def __init__(self,n,r):
        a.__init__(self,n)
        self.roll=r
    #def display(self):
        #print(self.name)
        #print(self.roll)
class c(b):
    def __init__(self,n,r,g):
        b.__init__(self,n,r)
        self.gender=g
    def show1(self):
        print(self.name)
        print(self.roll)
        print(self.gender)
ob=c('priyanka',1,'F')
ob.show1()
