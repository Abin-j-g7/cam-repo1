class bala():
    def __init__(self):
        self.__balance=6000
    def get_balan(self,balanc):
        if balanc>self.__balance:
            self.__balance=balanc
        return self.__balance
    # def set_balan(self,balanc):
    #     if balanc>self.__balance:
    #         self.__balance=balanc
            


ob=bala()
# ob.set_balan(5000)
a=ob.get_balan(7000)
print(a)
    