a=int(input("enter a number:"))
i=2
b=[]
while i<a:
    if a%i==0:
        b.append(i)
    i+=1
if a==0 or a==1:
    print(f"{a} is not a prime number")
elif len(b)==0:
    print(f"{a} is a prime number")
else:
    print(f"{a} is not a prime number")

