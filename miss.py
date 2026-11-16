a=[0,1,2,3,5,9]

i=0
while i<len(a):
    if i+1<len(a):
        if a[i+1]-a[i]!=1:
            d=a[i+1]-a[i]
            for j in range(1,d):
                print(a[i]+j)

    i+=1
