n=int(input("enter the number:"))
count=0
while n!=0:
    rem = n//10
    n=rem
    count+=1
print("the count of the numbers is",count)
