#WAP in python to create the following pattern.
    #1 1 1 1
    #2 2 2 2
    #3 3 3 3
    #4 4 4 4
def main(n):
    for i in range(1,n+1):
       for j in range(1,n+1):   
            print(i,end=' ')
            
       print()
        
        
if __name__=='__main__':
    n=int(input("enter the value of n: "))
    s=main(n)
        
