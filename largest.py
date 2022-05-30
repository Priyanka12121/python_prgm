#WAP in python to a function that will return the largest number among three integers.
def main(n1,n2,n3):
    
    if n1>n2 and n1>n3:
        return n1
    elif n2>n1 and n2>n3:
        return n2
    else:
        return n3
if __name__=='__main__':
    n1=int(input("enter the first no"))
    n2=int(input("enter the second no"))
    n3=int(input("enter the third no"))
    r=main(n1,n2,n3)
    print(r,"is largest")
