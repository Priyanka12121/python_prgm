r=int(input("Enter the no of row : "))
c=int(input("Enter the no of column: "))
g=[[0 for i in range(r)]for j in range(c)]
print("Enter the elements: ")
a=[[int(input())for i in range(r)]for j in range(c)]
for i in range(r):
    for j in range(c):
        g[i][j]=a[j][i]
print("original matrix:")
for i in range(r):
    for j in range(c):
        print(a[i][j],end=' ')
    print()
print("new matrix:")
for i in range(r):
    for j in range(c):
        print(g[i][j],end=' ')
    print()
        

        
























































