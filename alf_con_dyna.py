a=int(input("enter the number of rows:"))
k=0
for i in range(1,a+1):
    for j in range(i):
        print(chr(65+k)," ",end="")
        k+=1  # increment
    print()