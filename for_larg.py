limit=int(input("enter the limit:"))
large=0
for i in range(limit):
    a=int(input("enter the number:"))

    if a>large:
        large=a
    else:
        large=large
        

print(large ,"is the largest number")
    