def reverse(s):
    if s!='':
        return s[-1]+reverse(s[:-1])
    else:
        return s
s=input("enter the string")
print(reverse(s))                         
