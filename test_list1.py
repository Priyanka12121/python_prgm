import copy
l=[1,2,3,4,5]
l1=copy.deepcopy(l)
l1[0]=9
print(l)
print(l1)
