#series:1+1/2+1/3+1/4.....1/n
def main():
    n=int(input("enter the value of n"))
    s=0
    for i in range(1,n+1):
        s=s+(1/i)
        
    print(s)
main()   
