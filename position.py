n=int(input("enter a four digit no "))
t=n
f=4
p=1
s=0
while t!=0:
    
    a=t%10
    if f%2==0:
        s=s+a
    elif f%2!=0:
        p=p*a
    f=f-1
    t=t/10
print("sum of the digits at even position "+str(s))
print("product of the digits at odd position "+str(p))
    
