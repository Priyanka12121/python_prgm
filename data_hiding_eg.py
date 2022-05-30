class student:
    def __init__(self,n,r):
        self.name=n
        self.__roll=r
    def show(self):
        print(self.name)
        print(self.__roll)
s1=student('priyanka',1)
s1.show()
print(s1.name)
print(s1.__roll)
