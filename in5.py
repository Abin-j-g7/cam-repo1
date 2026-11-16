# hybrid inheritence

# class a:
#     pass
# class B(a):
#     pass
# class C(a):
#     pass
# class D(B,C):
#     pass


class vehicle:
    def drive(self):
        print("why are you driving the car")
class car(vehicle):
    def bike(self):
        print("bike is far better than car")
class elctri(vehicle):
    print("elstric")
class scooty(car,elctri):
    pass

ob=scooty()
ob.drive()
ob.bike()
