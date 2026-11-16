a={1,2,3,4,5}
b={2,4,6,8,7}

#union
print(a|b)
#intersection
print(a&b)
#difference
print(a-b)
print(b-a)

print(a.issubset(b))
print(a.isdisjoint(b))
print(a.intersection_update(b))
print(a)

