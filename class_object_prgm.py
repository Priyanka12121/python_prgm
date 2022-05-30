class student:
    def given_data(self, r, n):
        self.roll = r
        self.name = n
    
    def show_data(self):
        print(self.roll)
        print(self.name)

s1 = student()
s1.given_data(1,"Priyanka")
s1.show_data()
s2 = student()
s2.given_data(2,"Ashmita")
s2.show_data()
