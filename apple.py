#apple_problem
l=eval(input('enter the elements of list'))
count=0
m=sum(l)
no_b=len(l)
s=m//no_b
if m%no_b==0:
    ind=no_b-1
    while ind>=0:
        if ind==no_b-1:
            rind=0
        else:
            rind=ind+1
        if ind==0:
            lind=no_b-1
        else:
            lind=ind-1
    while (l[rind]<sh and l[ind]>5):
        l[rind]=l[rind]+1
        l[ind]=l[ind]-1
        count=count+1
        print(l)
        while(l[ind]>sh):
            l[lind]=l[ind]+1
            l[ind]=l[ind]-1
            count=count+1
            print(l)
    ind=ind-1
