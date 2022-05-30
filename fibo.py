#7 wap in python to create the following series.
# 0 1 1 2 3 5 8 13 21....n terms
def fibo(n):
    a=0
    b=1
    for i in range(1,n+1):
        print(a,end=',')
        c=a+b
        a=b
        b=c

def main():
    n=int(input("enter the value of n"))
    fibo(n)
if __name__=='__main__':
    main()
