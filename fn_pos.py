a=int(input("enter a number:"))

def pos(a):
    if a==0:
        print(f"{a} is zero")
    elif a<0:
        print(f"{a} is a negative number")
    elif a>0:
        print(f"{a}  is a positive number")

pos(a)