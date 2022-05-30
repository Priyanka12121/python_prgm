#Write a function repfree(s) that takes as input a string s and checks whether any 
#character appears more than once. The function should return True if there are no repetitions 
#and False otherwise. 

def repfree(s):
    for i in s:
        f=0
        for j in s:
            if i==j:
                f=f+1
                if f>1 :
                    return 0
    return 1
st=input("enter the string : ")
m=bool(repfree(st))
print(m)
    
        
