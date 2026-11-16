def facto(n):
    if n==0 or n==1:
        return 1
    else:
        return n*facto(n-1)   #functin/method
a=int(input("enter a number:"))
res=facto(a)
print(f"{res} is the factorial of {a}")