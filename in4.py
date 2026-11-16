# Heirarchical inheritence

class A:
    def sorry(self):
        print("i am sorry")
class B(A):
    def hei(self):           
        print(" say hai!")
class C(A):
    pass

ob=C()
ob1=B()

ob.sorry()
ob1.sorry()