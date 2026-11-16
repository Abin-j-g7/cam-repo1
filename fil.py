
from my_fact import facto

a=list(map (int,input("entr the numbers:").split()))

res= list(map(lambda x:x*x,a))    #map
hai=list(filter(lambda x:x%2==0,res))   #filter
print(res)
print(hai)
print(facto(5))

buy= list(filter(lambda x:x%2==0,map(lambda x:x*x,a))) #filter and map combined
print(buy)