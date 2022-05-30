#input:1126234
#output:[4,3,2,6,1]
l=[]
l1=[]
def recur(n):
    global l
    if n>0:
        t=n%10
        l.append(t)
        recur(n=n//10)
    return l
num=int(input("enter the number"))
l1=recur(num)
print(l1)
        
