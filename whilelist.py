a=[1,2,4,'abin','hai',34,'bye',56,'hei',78,7.5]

#integers=list(map(int,input("enter numbers:").split()))
#strings=list(map(str,input("enter the strings:").split()))
#floatnew=list(map(float,input("enter the floating point numbers:").split()))

#newlist=[]
#newlist=integers + strings + floatnew
#print(newlist)

b=[]
s=[]
n=0

while n<len(a):
    if type(a[n])==int:
        b.append(a[n])
    elif type(a[n])==str:
        s.append(a[n])
    else:
        print(a[n] ,'is',type(a[n]))
    n+=1
print(b,"is the collection of integers")
print(s,"is the collection of strings")