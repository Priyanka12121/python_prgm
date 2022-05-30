l=[[0 for i in range(4)]for x in range(5)]
l[0][0]=10
print(id(l[0]))
print(id(l[1]))
print(l[0]is l[1])
