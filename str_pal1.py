a=input("enter the string:")
n=len(a)
b=""
for i in range(n):
    b+=a[n-i-1]
if a==b:
    print(f"{a} is a palindrome")
else:
    print(f"{a} is not a palindrome")
