a=int(input("enter a string:"))
b=a
rem=0
while b!=0:
    rem+=b%10
    rem*=10
    b//=10
rem//=10
if a==rem:
    print(f"{a} is a palindrome")
else:
    print(f"{a} is not a palindrome")