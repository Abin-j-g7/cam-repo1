#encapsulation - public


class A:
    def my(self,name):
        self._name=name
    
class B(A):
    def hai(self):
        print(self._name)

o=B()
o.my('hai')
o.hai()
# print(o._name)
             
       
