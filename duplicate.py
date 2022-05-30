l1=[1,1,2,3,3,4,5,6,6,8,10,12]
l=len(l1)
i=0
while(i<l-1):
    l2=l1[i]
    j=i+1
    while(j<l-1):
        if l2==l1[j]:
            k=i
            while(k<l-1):
                l1[k]=l1[k+1]
                k=k+1
            l=l-1 
        j=j+1
    i=i+1
    
for i in range(0,l):
    print(l1[i],end='')

     
            
            
