def main():
    n=int(input("enter the number:"))
    c=0
    for i in range(2,n):
        if(n%i==0):
            c=c+1
    if(c>1):
        print("not prime number")
    else:
        print("prime number")
if __name__=='__main__':
    main()
