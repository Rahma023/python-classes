class Account:
    
    def __init__(self,name,phone_number):
        self.name=name
        self.phone_number=phone_number

        self.balance=0

    def show_balance(self):
      return f"Hello {self.name} your balance is {self.balance}"

    def deposite(self,amount):
      if amount > self.balance:
         return f"Hello {self.name} your balance is {self.balance} "
      else:
        self.balance-=amount
        return f"Hello {self.name} you cannot withdraw {self.show_balance()}"

    def withdraw(self,amount):
      if amount > self.balance:
        return f"Hello {self.name} your balance is {self.balance} you cannot withdraw {amount}"

      else:
        self.balance-=amount
        return f"Hello {self.name} you have deposited {amount} Ksh you cannot withdraw {self.show_balance()} "

    def borrow(self,amount):
      return f"Hello {self.name} you have taken a loan of {amount} "

    def repay(self,amount):
      return f"Hello {self.name} you have repaid a loan of {amount} "




        




    

    