hai="abcde"
for i in range(1,5):
    #print(" "*(4-i),end="")
    for j in range(i):
        print(hai[i-1]," ",end="")
    print()