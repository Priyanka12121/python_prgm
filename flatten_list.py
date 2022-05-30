def flatten(l,l1):
    if len(l)==0:
        return l1
    else:
        for i in l:
            if type(i)!=list:
                l1.append(i)
            else:
                flatten(i,l1)
    return l1
l=[1,2,[3,4],5,[6,7,8],9,10]
l1=[]
print(flatten(l,l1))
    
