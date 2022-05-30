class student:
    count=1
    def __init__(self, n):                 #constructor
        self.name = n
        self.roll = student.count
        student.count+=1                    #class variable
    
    def __str__(self):
        #print(self.name,self.roll)
        #print(student.count)
        return('Name:'+self.name,'Roll:'+str(self.roll))
    def __del__(self):
        print('Destructor call')
        
s1=student('Priyanka')
#s1.show_data()
#print(s1)
print(s1.__str__())
s2=student('Ashmita')
#s2.show_data()
#print(s2)
print(s2.__str__())
s3=student('Suvankar')
del s3


