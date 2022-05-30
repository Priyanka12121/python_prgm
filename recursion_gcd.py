#wap to calculate gcd of two natural no.
def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)
a=int(input("enter the first no"))
b=int(input("enter the second no"))
print(gcd(a,b))
    
