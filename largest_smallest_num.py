n=int(input("enter first no"))
n1=int(input("enter second no"))
n2=int(input("enter third no"))
l=n
if n1>l:
    l=n1
elif n2>l:
    l=n2
s=n
if n1<s:
    s=n1
elif n2<s:
    s=n2
print("largest number is "+str(l)+"smallest number is "+str(s))
