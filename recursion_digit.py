#Write a recursive function that  takes number as input parameter and print digits.
#input 13456
#output 1,3,4,5,6

def recur(n):
    global s,st
    if n>0:
        t=n%10
        s=str(t)
        st=s+','+st
        recur(n=n//10)
    return st

num=int(input("enter the number"))
s=""
st=""
wd=recur(num)
print(wd)
    
