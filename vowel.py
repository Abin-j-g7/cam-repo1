s=input("enter the  string:")
a="aeiouAEIOU"
COUNT=0
for i in s:
    if i in a:
        COUNT+=1
print(f"the count of wowels is:{COUNT}")