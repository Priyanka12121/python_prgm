#WAP in python to reverse a integer.
#input:12345678
#output:87654321
def main(n):
    s=0
    while(n!=0):
        t=n%10
        s=s*10+t
        n=n//10
    return s
 
if __name__=='__main__':
    n=int(input("enter the value of n: "))
    r=main(n)
    print(r)
        
