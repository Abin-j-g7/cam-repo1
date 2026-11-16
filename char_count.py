c=input("enter a word:")
cn=input("enter a character to find its count:")
count=0
len=len(c)
#print(len)
for i in range(len):
    if c[i]==cn:
        count+=1
print("count of ",cn,"is",count)