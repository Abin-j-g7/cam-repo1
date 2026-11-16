a=[1,2,4,'abin','hai',34,'bye',56,'hei',78,7.5]

b=a[3:7]+a[2:7]
c=a[-3:-1]
b.reverse()
print(a)
a.extend([1,4])
a.insert(-3,100)

print(a)
a.pop()
del a[2:4]
a.remove(2)
#a.sort()
b=a.copy()
print(b)
print(a.count(1))