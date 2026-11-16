limit=int(input("enter your limit"))
n=int(input("enter the number of rows"))

while n<limit:
    n=+1
    if(n%3!=0):
        continue
    print(n)
else:
    print("your limit reached")
