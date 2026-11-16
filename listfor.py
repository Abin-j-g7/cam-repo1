a=[1,2,4,'abin','hai',34,'bye',56,'hei',78,7.5]
b=[]
s=[]
#for i in a:
    #print(i)
for i in a:
    if type(i)==int:
        b.append(i)
    elif type(i)==str:
        s.append(i)
    else:
        print(i,"is",type(i))

print(b)
print(s)