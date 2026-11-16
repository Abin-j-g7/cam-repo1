a=list(map(int,input("enter the marks of the students:").split()))
i=0
while i<len(a):
    if a[i]>10:
        print(a[i])
    i+=1