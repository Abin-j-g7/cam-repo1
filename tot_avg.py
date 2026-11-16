n=int(input("enter te number of subjects:"))
tot=0
for i in range(n):
    mark=int(input("enter the mark each subject:"))
    tot+=mark
print("total mark is:",tot)
avg=tot//n
print("the average mark is:",avg)

