print("the odd numbers  under 10 are:")
for i in range(1,10,2):
    print(i)
print("the even numbers  under 10 are:")
for i in range(0,11,2):
    print(i)

print("the reverse  of numbers upto 10 is:")
for i in range(10,0,-1):
    print(i)


a=int(input("enter the number:"))

print("the multiplication table of",a,"is:")
for i in range(1,11):
    print(i,"*",a,"=",a*i)