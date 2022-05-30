class a:
    def fun1(self):
        print('in class a')
class b(a):
    def fun2(self):
        print('in class b')
ob1=a()
ob1.fun1()
ob2=b()
ob2.fun2()
ob2.fun1()
