#function polymorphism

class A:
    def add(self,a,b=30):
        print(f"result is:{a+b}")
class B(A):
    def add(self,a,b=2):
        print(f"result is:{a+b}")
class C(B):
    def add(self,a,b=4):
        print(f"result is:{a+b}")
o=A()
o.add(2,3)
o.add(2)


v=B()
v.add(2,5)
v.add(2)

