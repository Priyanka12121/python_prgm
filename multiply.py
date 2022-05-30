#Write a recursive function that multiplies two positive no a and b and returns the result. multiplication is to be achieve is a+a+a...b times
sum=0
def multi(a,b):
    global sum
    if b>0:
        sum=sum+a
        b=b-1
        multi(a,b)
    return sum
    
def main():
    a,b=map(int,input("enter the value of a and b: " ).split())
    s=multi(a,b)
    print(s)
main()
        

    
