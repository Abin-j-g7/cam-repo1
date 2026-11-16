a=int(input("enter the number of rows:"))

for i in range(1,a+1):
    for j in range(i):
        print(chr(65+j)," ",end="")
    print()