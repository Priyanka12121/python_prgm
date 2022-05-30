def main():
    n=int(input("enter the number: "))
    print ("divisor are :")
    for i in range(2,n):
        if(n%i==0):
            print(i)

if __name__=='__main__':
    main()
