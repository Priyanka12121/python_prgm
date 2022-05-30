# input=11362
# output=26311

def func(n):
    if n>0:
        t=n%10
        print(t,end=',')
        func(n=n//10)
num=int(input("enter the number"))
func(num)
