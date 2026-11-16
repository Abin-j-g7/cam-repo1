a=int(input("enter the first  number:"))
b=int(input("enter the second number:"))
op=input("enter an operator:")

def calculator(a,b,opp):
    if opp=="+":
        return a+b
    elif opp=="-":
        return a-b
    elif opp=="*":
        return a*b
    elif opp=="/":
        return a/b
    elif opp=="%":
        return a%b

res=calculator(a,b,op)
print(f"{a}{op}{b} is {res}")