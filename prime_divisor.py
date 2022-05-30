def prime(n):
    c=0
    for i in range(2,n):
        if n%i==0:
            c=c+1
            break
    return c
def main():
    n=int(input("enter the number"))
    i=2
    while i<=n:
        if n%i==0:
            d=prime(i)
            if d==0:
                 print(i,end=',')
                 n=n/i
        else:
            i=i+1
            
main()

        
    
