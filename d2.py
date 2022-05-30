#[1,3,4,1,6,10,2,3,8,6,2,12,4]
lst=eval(input('enter the elements'))
i=0
while i<len(lst)-1:
    p=i
    j=i+1 
    while j<len(lst):
        if lst[j]==p:
            lst.pop(j)
        j=j+1
    i=i+1
print(lst)
       
