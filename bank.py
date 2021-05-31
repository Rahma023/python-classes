from datetime import datetime
class Account:
    def __init__(self,name,phone_number):
        self.name=name
        self.phone_number=phone_number

        self.balance=0
        self.statement=[]

    def show_balance(self):
      return f"Hello {self.name} your balance is {self.balance}"

    def deposit(self,amount):
      if amount < self.balance:
         return f"Hello {self.name} your balance is {self.balance} "
      else:
        self.balance+=amount
        now=datetime.now()
        transaction={"amount":100, "time":now, "narration":"deposited"}
        self.statement.append(transaction)
        return f"Hello {self.name} you cannot withdraw {self.show_balance()}"

    def show_statement(self):
      for transaction in self.statement:
        amount=transaction["amount"]
        narration=transaction["narration"]
        time=transaction["time"]
        date=time.strftime("%d/%m/%y")
        print(f"{date} : {narration}  {amount} ")
      return

    def withdraw(self,amount):
      if amount > self.balance:
        return f"Hello {self.name} your balance is {self.balance} you cannot withdraw {amount}"

      else:
        self.balance-=amount
        now=datetime.now()
        withdrawal={"amount":200, "time":now, "narration":"deposited"}
        self.statement.append(withdrawal)
       

        return f"Hello {self.name} you have deposited {amount} Ksh you cannot withdraw {self.show_balance()} "

    def borrow(self,amount):
      return f"Hello {self.name} you have taken a loan of {amount} "

    def repay(self,amount):
      return f"Hello {self.name} you have repaid a loan of {amount} "               




        




    

    