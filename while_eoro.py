ev=0
od=0
n=int(input("enter a number:"))
while n!=0:
    if n%2==0:
        ev+=1
    else:
        od+=1
    n=int(input("enter a number:"))
print("even count is:",ev)
print("odd count is:",od)
