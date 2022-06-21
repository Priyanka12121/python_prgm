a=int(input("enter the first side of triangle"))
b=int(input("enter the second side of triangle"))
c=int(input("enter the third side of triangle"))
if a==b and a==c:
    print("triangle is equilateral")
elif a!=b and b!=c and c!=a:
    print("triangle is scalene")
elif a==b or b==c or c==a:
    print("triangle is isosceles")
