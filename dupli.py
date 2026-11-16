a=list(map(int,input("enter the marks of the students:").split()))

for i in a:
    c=a.count(i)
    if c>1:
        a.remove(i)
print(a)
                