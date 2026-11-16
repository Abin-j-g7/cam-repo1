a={'abin':2,'chris':3,'sid':4}
print(a.get('abin',0))
print(a.get('ab',0))
print(a['abin'])
a['hai']=34
b={'abin':2,'chris':3,'sid':4}
print(b)
print(a.update({'palce':'kochi','bye':'ok'}))
print(a.fromkeys(b))
print(a)
c=a.pop('abin')
print(a)
print(c)
a.popitem()
print(a.keys())
print(a.values())
print(a.items())

print(a)

for i,j in a.items():
    #print(i,":",a[i])
    print(i,":",j)