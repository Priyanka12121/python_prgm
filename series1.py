#WAP in python to find the x of the following series using the conceptg of function.you need to pass n to the function and return x from it.
# x=1*2*3*4...*n
def main(n):
    x=1
    for i in range(1,n+1):
          x=x*i
    return x        
if __name__=='__main__':
    n=int(input("enter the value of n: "))
    s=main(n)
    print("result of series is",s)    
