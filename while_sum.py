n=int(input("enter the number:"))
tot=0
while n!=0:
    r=n%10
    tot+=r
    rem=n//10
    n=rem
print("the sum of numbers is:",tot)