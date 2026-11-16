a=int(input("enter a number:"))

def p(a,i=a-1):
    if i!=0:
        print(a-i)
        i-=1
        p(a,i)
    else:
        return
   

p(a)
print(a)