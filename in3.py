#Multi - level inheritence

# class A:
#     def sorry(self):
#         print("i am sorry")
# class B(A):
#     def hei(self):           # B inherits the properties of A , C inherits the properties of B, that is called multi level inheritence 
#         print(" say hai!")
# class C(B):
#     pass

# ob=C()

# ob.sorry()
# ob.hei()


class vehicle:
    def drive(self):
        print("why are you driving the car")
class car(vehicle):
    def bike(self):
        print(" bike is far better than car")
class elctri(car):
    pass

ob=elctri()
ob.drive()
ob.bike()
