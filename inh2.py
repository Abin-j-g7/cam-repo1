# multiple inheritence

class father:
    def sorry(self):
        print("i am sorry")
    def hei(self):
            print("hai!")              
class mother:
    def hei(self):
        print(" say hai!")
    def sorry(self):
            print("sorry")
class C(father,mother):               # python follows MRO protocol - if we write same methods in father and mother and call the method name using object, then the firest class theat is assigned to the class c will be taken.
    pass                              # since father is the first class in the brackets,so the priority will be given to father class 

ob=C()

ob.sorry()
ob.hei()