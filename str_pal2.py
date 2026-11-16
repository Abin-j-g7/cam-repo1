a=input("enter the string:")
n=len(a)
b=[]
for i in range(n):
    b.append(a[n-i-1])
reversed_string=''.join(b)
if a==reversed_string:
    print(f"{a} is a palindrome")
else:
    print(f"{a} is not a palindrome")