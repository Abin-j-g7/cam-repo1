a=int(input("enter a number:"))
b=a
c=a
n=0
rem=0
while a!=0:
    a//=10
    n+=1

while b!=0:
    rem+=(b%10)**n
    b//=10

if c==rem:
    print(f"{c} is a amstrong number")
else:
    print(f"{c}  is not an amstrong number")
