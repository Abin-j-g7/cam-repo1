#method overriding

class A:
    def A(self):
        print("A")
class B(A):
    def Aself():
        print("B")
class C(B):
    def A(self):
        print("C")
ob=C()
ob.A()
