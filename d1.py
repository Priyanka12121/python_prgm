#[1,1,2,3,3,4,5,6,6,8,10,12]
lst=eval(input('enter the elements'))
i=0
while i<len(lst)-1:
    j=i
    while j<len(lst)-1:
        if lst[j]==lst[j+1]:
            lst.pop(j+1)
        j=j+1
    i=i+1
print(lst)
       
        
        
        
            
