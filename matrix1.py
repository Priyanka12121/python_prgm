r=int(input("enter the no of row: "))
c=int(input("enter the no of column:"))
a=[[int(input("enter the elements"))for i in range(r)]for j in range(c)]
g=[[0 for i in range(c)]for j in range(r)]
l=[]
k=0
for i in range(r):
   for j in range(c):
        l[k]=a[i][j]
        k=k+1
t=0

for i in range(c):
   for  j in range(r):
        g[i][j]=l[t]
        t=t+1
        
print("original matrix:")
for i in range(r):
    for j in range(c):
        print(a[i][j],end=' ')
    print()
    
print("new matrix:")
for i in range(c):
    for j in range(r):
        print(g[i][j],end=' ')
    print()
        
   
       
   
