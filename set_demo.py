num={1,2,3,4,2}
for i in num:
    print(i)
#n=set(num)
#num=list(n)
#print(num)
#print(list(set(num)))
#n=set()
#print(type(num))
#print(type(n))

num.add(6)
print(num)

#discard

num.discard(20)
print(num)

#remove

num.remove(3)
print(num)

#add
num.add(45)
print(num)

#update

num.update([30,40,50])
print(num)

#pop
num.pop()
print(num)

#clear

num.clear()
print(num)