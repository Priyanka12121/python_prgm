class a:
    def __init__(self,n):
        self.name=n
    def show(self):
        print('name:',self.name)
class b(a):
    def __init__(self,n,r):
        a.__init__(self,n)
        self.roll=r
    def display(self):
        print(self.name)
        print(self.roll)
ob=b('priyanka',1)
ob.display()
