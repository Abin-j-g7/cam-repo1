class Ob:       #class creation
    name="abin" #class attributes/variables
    age=18
    def __init__(self,name="nil",age="unknown"):   #constructor
        self.name=name
        self.age=age
   
    def p(self):
        print(f"your name is:{self.name}")
        print(f"your age is:{self.age}")

    

c1=Ob("chris",18)  #object creation
c2=Ob()


c1.p()
print(c2.name)