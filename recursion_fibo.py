#nth term of fibbonacci series
#1 1 2 3 5 8 13 21......

def fibo(n):
    if n<0:
        print("incorrect input")
    elif n==0:
        return 0
    elif n==1 or n==2:
        return 1
    else:
        return fibo(n-1)+fibo(n-2)
               
n= int(input("enter the value of n"))
print(n," term is: ",fibo(n))
    
