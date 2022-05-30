#print the series using function concept in python.
#1,3,5,7....n
def main():
    n=int(input("enter the value of n: "))
    for i in range(1,n+1):
          if i%2!=0:
              print(i ,end=',')
            
if __name__=='__main__':
    main()
          
