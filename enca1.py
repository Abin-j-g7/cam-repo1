class A:
    def __init__(self,name):
        self.__name=name
    def hai(self):
        print(self.__name)
    
# class B(A):
#     def hai(self):
#         print(self.__name)

o=A('hai')
o.hai()
print(o.__name)