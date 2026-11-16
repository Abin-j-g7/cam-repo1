a=[0,1,2,3,5,9]
b=min(a)
c=max(a)
for i in range(b,c):
    if i not in a:
        print(i)