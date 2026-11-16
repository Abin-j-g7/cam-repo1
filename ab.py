from abc import ABC,abstractmethod

class A(ABC):
    @abstractmethod
    def hai(self):
        pass
    def hello(self,hai):
        self.name=hai
        print(self.name)
class B(A):
    def hai(self,name):
        self.name=name
        print(self.name)

ob=B()
ob.hai('ab')
ob.hello('abin')
