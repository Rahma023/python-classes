from datetime import datetime

class Account:
    def __init__(self,name,phone_number):
        self.name=name
        self.phone_number=phone_number

        self.balance=0
        self.statement=[]
        self.loan=0
        

    def show_balance(self):
      return f"Hello {self.name} your balance is {self.balance}"

    def deposit(self,amount):
      try:
        10+amount
      except TypeError:
        return f"The amount must be in figures"
      if amount < self.balance:
         return f"Hello {self.name} your balance is {self.balance} "
      else:
        self.balance+=amount
        now=datetime.now()
        transaction={"amount":100, "time":now, "narration":"deposited"}
        self.statement.append(transaction)
        return f"Hello {self.name} your balance is {self.balance} "
        # return f"Hello {self.name} you cannot withdraw {self.show_balance()}"

    def show_statement(self):
      for transaction in self.statement:
        amount=transaction["amount"]
        narration=transaction["narration"]
        time=transaction["time"]
        date=time.strftime("%d/%m/%y")
        print(f"{date} : {narration}  {amount} ")
      return

    def withdraw(self,amount):
      try:
        0+amount
      except TypeError:
        return f"The amount must be in figures"
      if amount > self.balance:
        return f"Hello {self.name} your balance is {self.balance} you cannot withdraw {amount}"

      else:
        self.balance-=amount
        now=datetime.now()
        withdrawal={"amount":200, "time":now, "narration":"deposited"}
        self.statement.append(withdrawal)
       

        return f"Hello {self.name} you have deposited {amount} Ksh you cannot withdraw {self.show_balance()} "
        
    def borrow(self,amount):
      try:
        1+amount
      except TypeError:
        return f"The amount must be in figures"
      if amount < 0:
        return f"Hello {self.name} your amount should be more than 0 "
      elif self.loan > 0:
        return f"Hello {self.name} you already have a loan " 
     
      elif amount < 0.1*self.balance:
        return f"Hello {self.name} you cannot have a loan your loan limit is {0.05*self.balance} "
      else:
        loan=amount*1.05
        self.loan=loan
        self.balance += amount
        self.balance-= amount
        now=datetime.now()
        transaction={"amount":4000, "time":now, "narration":"deposited"}
        self.statement.append(transaction)
        return f"{self.show_balance()} and your new balance is {self.balance} "

    def repay(self,amount):
      try:
        1+amount
      except TypeError:
        return f"The amount must be in figures"
      if amount < 0:
        return f"Hello {self.name} you have not repaid a loan of {amount} "  
      elif amount <= self.loan:
        self.loan -= amount
        return f"Hello {self.name} you have repaid  {amount} "
      else:
        diff=amount-self.loan
        self.loan=0
        self.deposit(diff)
        now=datetime.now()
        transaction={"amount":300, "time":now, "narration":"deposited"}
        self.statement.append(transaction)
        return f"Hello {self.name} you have repaid your loan of {self.show_balance()} and your new balance is {diff} "

    def transfer(self,account,amount):
      try:
        0+amount
      except TypeError:
        return f"The amount must be in figures"
      fee=amount*0.05
      total=amount+fee
      if total>self.balance:
        return f"Hello {self.name} your balance is {self.balance} and you need atleast {total} for this transfer"
      elif total>self.balance: 
       return f"You have insufficient {self.balance}"
      else:
        self.balance-=total
        account.deposit(amount)

class MobileMoneyAccount(Account):
    def __init__(self, name, phone_number, service_provider):
      Account.__init__(self,name, phone_number)
      self.service_provider=service_provider

    def buy_airtime(self, amount):
      try:
        0+amount
      except TypeError:
        return f"The amount must be in figures"
      if amount>0:
        return f"Hello {self.name} your balance is {amount}"
      elif self.balance<amount:
        return f"Hello {self.name} your amount is low"
      else:
        self.balance-=amount
        return f"Hello {self.name} you bought airtime of {amount}"



      
        
        
        
