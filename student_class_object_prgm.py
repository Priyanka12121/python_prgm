class student:
    def __init__(self,n,r):
        self.name=n
        self.rollNum=r
    def setMarks(self):
        self.marklist=eval(input("enter the marks in five subjects: "))
    def getStream(self):
        self.stream=input("enter the stream:")
        if self.stream =='A':
            self.stream="Arts"
        elif self.stream =='C':
            self.stream="Commerce"
        elif self.stream=='S':
            self.stream="Science"
    def percentage(self):
        self.percentage=sum(self.marklist)/len(self.marklist)
    def gradGen(self):
        if(self.percentage>=90):
            self.grade='A'
        elif(self.percentage<90 and self.percentage>=80):
            self.grade='B'
        elif(self.percentage<80 and self.percentage>=65):
            self.grade='C'
        elif(self.percentage<65 and self.percentage>=40):
            self.grade='D'
        elif(self.percentage<40 ):
            self.grade='E'
    def showData(self):
        print("Name: ",self.name)
        print("Rollnum: ",self.rollNum)
        print("Stream: ",self.stream)
        print("Percentage: ",self.percentage)
        print("Grade: ",self.grade)
        
ob=student('Priyanka',2)
ob.setMarks()
ob.getStream()
ob.percentage()
ob.gradGen()
ob.showData()
