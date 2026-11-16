# class A:
#     def drive(self):
#         print("drive fasst")
# class B(A):
#     def drive(self):            # Method Overriding  -   it is the process in which the child class method overrides the method of parent class.( it happens when there are mehods with same name  each class)  )
#         super().drive()
#         print("drive slow")     # this can be ovecome using "super" keyword
# c=B()                           # super() - we want to execute both the parent class method and the child class method // super().method_name()
# c.drive()



class A:
    def __init__(self):
        print("drive fasst")
class B(A):
    def __init__(self):            # Method Overriding  -   it is the process in which the child class method overrides the method of parent class.( it happens when there are mehods with same name  each class)  )
        super().__init__()
        print("drive slow")     # this can be ovecome using "super" keyword
c=B()                           # super() - we want to execute both the parent class method and the child class method // super().method_name()
