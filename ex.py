

class BankError(Exception):
    pass

class bank:
    def __init__(self):
        self.balance=3000
    def deposit(self,balan):
        self.balance+=balan
    def withdraw(self,withd):
        if withd>self.balance:
           raise BankError("no Enough balance")
        else:
            self.balance-=withd
            return ("withdrawn succesfully")


try:
    obj = bank()
    print(obj.withdraw(2000))
except BankError as e:
    print("error",e)
          
     
               

        